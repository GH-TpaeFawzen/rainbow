# ----------------------------------------------------------------------
# rainbow, a command line colorizer
# Copyright (C) 2011-2017 Julien Nicoulaud <julien.nicoulaud@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import os
import signal
import sys
from textwrap import dedent
from threading import Timer

import pytest

from rainbow import ansi
from rainbow.command.execute import ExecuteCommand
from rainbow.transformer import ReplaceTransformer
from tests.test_utils import stdin_empty_all_variants, stdin_from_string_all_variants


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_true(capsys, stdin):
    with stdin:
        assert ExecuteCommand(['true']).run() == 0
        out, err = capsys.readouterr()
        assert out == ansi.ANSI_RESET_ALL
        assert err == ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_false(capsys, stdin):
    with stdin:
        assert ExecuteCommand(['false']).run() == 1
        out, err = capsys.readouterr()
        assert out == ansi.ANSI_RESET_ALL
        assert err == ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_identity(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            [sys.executable, '-c', dedent(r'''
                import sys
                sys.stdout.write('stdout\n')
                sys.stderr.write('stderr\n')
            ''')]
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'stdout\n' + ansi.ANSI_RESET_ALL
        assert err == 'stderr\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_identity_bash(capsys, stdin):
    with stdin:
        assert ExecuteCommand(['/bin/bash', '-c', 'echo "stdout"; echo "stderr" >&2']).run() == 0
        out, err = capsys.readouterr()
        assert out == 'stdout\n' + ansi.ANSI_RESET_ALL
        assert err == 'stderr\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_identity_mixed_stdin_and_err(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            [sys.executable, '-c', dedent(r'''
                import sys
                sys.stdout.write('stdout1\n')
                sys.stderr.write('stderr2\n')
                sys.stdout.write('stdout3')
                sys.stdout.write('stdout4\n')
                sys.stderr.write('stderr4')
                sys.stderr.write('stderr5\n')
            ''')]
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'stdout1\nstdout3stdout4\n' + ansi.ANSI_RESET_ALL
        assert err == 'stderr2\nstderr4stderr5\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_bufferized_output(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            [sys.executable, '-c', dedent(r'''
                import sys, time
                sys.stdout.write('stdout1\n')
                time.sleep(0.5)
                sys.stdout.write('stdout2\nstdout3\n')
                time.sleep(0.5)
                sys.stdout.write('stdout4\n')
            ''')]
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'stdout1\nstdout2\nstdout3\nstdout4\n' + ansi.ANSI_RESET_ALL
        assert err == ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_bufferized_partial_lines(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            [sys.executable, '-c', dedent(r'''
                import sys
                sys.stdout.write('std')
                sys.stdout.flush()
                sys.stdout.write('out1\nstdout2\n')
            ''')]
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'stdout1\nstdout2\n' + ansi.ANSI_RESET_ALL
        assert err == ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_unflushed_output(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            [sys.executable, '-c', dedent(r'''
                import sys
                sys.stdout.write('message')
            ''')]
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'message\n' + ansi.ANSI_RESET_ALL
        assert err == ansi.ANSI_RESET_ALL


@pytest.mark.timeout(2)
@pytest.mark.parametrize("stdin", stdin_from_string_all_variants('line\n'), ids=str)
def test_cat_stdin(capsys, stdin):
    with stdin:
        assert ExecuteCommand(['cat']).run() == 0
        out, err = capsys.readouterr()
        assert out == 'line\n' + ansi.ANSI_RESET_ALL
        assert err == ansi.ANSI_RESET_ALL


@pytest.mark.timeout(2)
@pytest.mark.parametrize("stdin", stdin_from_string_all_variants('line1\nline2\n'), ids=str)
def test_cat_stdin_two_lines(capsys, stdin):
    with stdin:
        assert ExecuteCommand(['cat']).run() == 0
        out, err = capsys.readouterr()
        assert out == 'line1\nline2\n' + ansi.ANSI_RESET_ALL
        assert err == ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_stdout_transformer(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            args=[sys.executable, '-c', dedent(r'''
                import sys
                sys.stdout.write('message\n')
                sys.stderr.write('message\n')
            ''')],
            stdout_transformer=ReplaceTransformer('message', 'REPLACED')
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'REPLACED\n' + ansi.ANSI_RESET_ALL
        assert err == 'message\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_stdout_transformer_bash(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            args=['/bin/bash', '-c', 'echo "message"; echo "message" >&2'],
            stdout_transformer=ReplaceTransformer('message', 'REPLACED')
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'REPLACED\n' + ansi.ANSI_RESET_ALL
        assert err == 'message\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_stderr_transformer(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            args=[sys.executable, '-c', dedent(r'''
                import sys
                sys.stdout.write('message\n')
                sys.stderr.write('message\n')
            ''')],
            stderr_transformer=ReplaceTransformer('message', 'REPLACED')
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'message\n' + ansi.ANSI_RESET_ALL
        assert err == 'REPLACED\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_stderr_transformer_bash(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            args=['/bin/bash', '-c', 'echo "message"; echo "message" >&2'],
            stderr_transformer=ReplaceTransformer('message', 'REPLACED')
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'message\n' + ansi.ANSI_RESET_ALL
        assert err == 'REPLACED\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_stdout_and_stderr_transformers(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            args=[sys.executable, '-c', dedent(r'''
                import sys
                sys.stdout.write('stdout\n')
                sys.stderr.write('stderr\n')
            ''')],
            stdout_transformer=ReplaceTransformer('stdout', 'STDOUT_REPLACED'),
            stderr_transformer=ReplaceTransformer('stderr', 'STDERR_REPLACED')
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'STDOUT_REPLACED\n' + ansi.ANSI_RESET_ALL
        assert err == 'STDERR_REPLACED\n' + ansi.ANSI_RESET_ALL


@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_stdout_and_stderr_transformers_bash(capsys, stdin):
    with stdin:
        assert ExecuteCommand(
            args=['/bin/bash', '-c', 'echo "stdout"; echo "stderr" >&2'],
            stdout_transformer=ReplaceTransformer('stdout', 'STDOUT_REPLACED'),
            stderr_transformer=ReplaceTransformer('stderr', 'STDERR_REPLACED')
        ).run() == 0
        out, err = capsys.readouterr()
        assert out == 'STDOUT_REPLACED\n' + ansi.ANSI_RESET_ALL
        assert err == 'STDERR_REPLACED\n' + ansi.ANSI_RESET_ALL


@pytest.mark.timeout(5)
@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_interrupted(stdin):
    with stdin:
        Timer(1.0, os.kill, [os.getpid(), signal.SIGINT]).start()
        assert ExecuteCommand(['sleep', '100']).run() == -2


@pytest.mark.skip(reason="Issue #17: encoding is not properly managed")
@pytest.mark.parametrize("stdin", stdin_empty_all_variants(), ids=str)
def test_malformed_utf8(stdin):
    with stdin:
        assert ExecuteCommand(['cat', 'tests/resources/UTF-8-test.txt']).run() == 0