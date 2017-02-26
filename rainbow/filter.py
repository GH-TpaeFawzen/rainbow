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

from .ansi import *


class Filter:
    def __init__(self, name, help, short_option=None, long_option=None, before=None, after=None):
        self.name = name
        self.help = help
        self.short_option = short_option
        self.long_option = long_option
        self.before = before
        self.after = after

    def __str__(self):
        return self.name


class FilterGroup:
    def __init__(self, name, help, filters):
        self.name = name
        self.help = help
        self.filters = filters

    def __str__(self):
        return self.name


FILTER_GROUPS = [
    FilterGroup(
        name='Foreground color',
        help='Use these options to associate patterns to text foreground colors.',
        filters=[
            Filter(name='foreground-red',
                   short_option='r',
                   long_option='red',
                   help='print pattern in red',
                   before=ANSI_FOREGROUND_RED,
                   after=ANSI_FOREGROUND_RESET),
            Filter(name='foreground-green',
                   short_option='g',
                   long_option='green',
                   help='print pattern in green',
                   before=ANSI_FOREGROUND_GREEN,
                   after=ANSI_FOREGROUND_RESET),
            Filter(name='foreground-yellow',
                   short_option='y',
                   long_option='yellow',
                   help='print pattern in yellow',
                   before=ANSI_FOREGROUND_YELLOW,
                   after=ANSI_FOREGROUND_RESET),
            Filter(name='foreground-blue',
                   short_option='b',
                   long_option='blue',
                   help='print pattern in blue',
                   before=ANSI_FOREGROUND_BLUE,
                   after=ANSI_FOREGROUND_RESET),
            Filter(name='foreground-magenta',
                   short_option='m',
                   long_option='magenta',
                   help='print pattern in magenta',
                   before=ANSI_FOREGROUND_MAGENTA,
                   after=ANSI_FOREGROUND_RESET),
            Filter(name='foreground-cyan',
                   short_option='c',
                   long_option='cyan',
                   help='print pattern in cyan',
                   before=ANSI_FOREGROUND_CYAN,
                   after=ANSI_FOREGROUND_RESET),
            Filter(name='foreground-red-before',
                   long_option='red-before',
                   help='toggle foreground to red on beginning of pattern',
                   before=ANSI_FOREGROUND_RED),
            Filter(name='foreground-green-before',
                   long_option='green-before',
                   help='toggle foreground to green on beginning of pattern',
                   before=ANSI_FOREGROUND_GREEN),
            Filter(name='foreground-yellow-before',
                   long_option='yellow-before',
                   help='toggle foreground to yellow on beginning of pattern',
                   before=ANSI_FOREGROUND_YELLOW),
            Filter(name='foreground-blue-before',
                   long_option='blue-before',
                   help='toggle foreground to blue on beginning of pattern',
                   before=ANSI_FOREGROUND_BLUE),
            Filter(name='foreground-magenta-before',
                   long_option='magenta-before',
                   help='toggle foreground to magenta on beginning of pattern',
                   before=ANSI_FOREGROUND_MAGENTA),
            Filter(name='foreground-cyan-before',
                   long_option='cyan-before',
                   help='toggle foreground to cyan on beginning of pattern',
                   before=ANSI_FOREGROUND_CYAN),
            Filter(name='foreground-reset-before',
                   long_option='reset-before',
                   help='reset foreground color on beginning of pattern',
                   before=ANSI_FOREGROUND_RESET),
            Filter(name='foreground-red-after',
                   long_option='red-after',
                   help='toggle foreground to red on end of pattern',
                   after=ANSI_FOREGROUND_RED),
            Filter(name='foreground-green-after',
                   long_option='green-after',
                   help='toggle foreground to green on end of pattern',
                   after=ANSI_FOREGROUND_GREEN),
            Filter(name='foreground-yellow-after',
                   long_option='yellow-after',
                   help='toggle foreground to yellow on end of pattern',
                   after=ANSI_FOREGROUND_YELLOW),
            Filter(name='foreground-blue-after',
                   long_option='blue-after',
                   help='toggle foreground to blue on end of pattern',
                   after=ANSI_FOREGROUND_BLUE),
            Filter(name='foreground-magenta-after',
                   long_option='magenta-after',
                   help='toggle foreground to magenta on end of pattern',
                   after=ANSI_FOREGROUND_MAGENTA),
            Filter(name='foreground-cyan-after',
                   long_option='cyan-after',
                   help='toggle foreground to cyan on end of pattern',
                   after=ANSI_FOREGROUND_CYAN),
            Filter(name='foreground-reset-after',
                   long_option='reset-after',
                   help='reset foreground color on end of pattern',
                   after=ANSI_FOREGROUND_RESET),
        ]
    ),
    FilterGroup(
        name='Background color',
        help='Use these options to associate patterns to text background colors.',
        filters=[
            Filter(name='background-red',
                   long_option='background-red',
                   help='print pattern with red background',
                   before=ANSI_BACKGROUND_RED,
                   after=ANSI_BACKGROUND_RESET),
            Filter(name='background-green',
                   long_option='background-green',
                   help='print pattern with green background',
                   before=ANSI_BACKGROUND_GREEN,
                   after=ANSI_BACKGROUND_RESET),
            Filter(name='background-yellow',
                   long_option='background-yellow',
                   help='print pattern with yellow background',
                   before=ANSI_BACKGROUND_YELLOW,
                   after=ANSI_BACKGROUND_RESET),
            Filter(name='background-blue',
                   long_option='background-blue',
                   help='print pattern with blue background',
                   before=ANSI_BACKGROUND_BLUE,
                   after=ANSI_BACKGROUND_RESET),
            Filter(name='background-magenta',
                   long_option='background-magenta',
                   help='print pattern with magenta background',
                   before=ANSI_BACKGROUND_MAGENTA,
                   after=ANSI_BACKGROUND_RESET),
            Filter(name='background-cyan',
                   long_option='background-cyan',
                   help='print pattern with cyan background',
                   before=ANSI_BACKGROUND_CYAN,
                   after=ANSI_BACKGROUND_RESET),
            Filter(name='background-red-before',
                   long_option='background-red-before',
                   help='toggle background to red on beginning of pattern',
                   before=ANSI_BACKGROUND_RED),
            Filter(name='background-green-before',
                   long_option='background-green-before',
                   help='toggle background to green on beginning of pattern',
                   before=ANSI_BACKGROUND_GREEN),
            Filter(name='background-yellow-before',
                   long_option='background-yellow-before',
                   help='toggle background to yellow on beginning of pattern',
                   before=ANSI_BACKGROUND_YELLOW),
            Filter(name='background-blue-before',
                   long_option='background-blue-before',
                   help='toggle background to blue on beginning of pattern',
                   before=ANSI_BACKGROUND_BLUE),
            Filter(name='background-magenta-before',
                   long_option='background-magenta-before',
                   help='toggle background to magenta on beginning of pattern',
                   before=ANSI_BACKGROUND_MAGENTA),
            Filter(name='background-cyan-before',
                   long_option='background-cyan-before',
                   help='toggle background to cyan on beginning of pattern',
                   before=ANSI_BACKGROUND_CYAN),
            Filter(name='background-reset-before',
                   long_option='background-reset-before',
                   help='reset background color on beginning of pattern',
                   before=ANSI_BACKGROUND_RESET),
            Filter(name='background-red-after',
                   long_option='background-red-after',
                   help='toggle background to red on end of pattern',
                   after=ANSI_BACKGROUND_RED),
            Filter(name='background-green-after',
                   long_option='background-green-after',
                   help='toggle background to green on end of pattern',
                   after=ANSI_BACKGROUND_GREEN),
            Filter(name='background-yellow-after',
                   long_option='background-yellow-after',
                   help='toggle background to yellow on end of pattern',
                   after=ANSI_BACKGROUND_YELLOW),
            Filter(name='background-blue-after',
                   long_option='background-blue-after',
                   help='toggle background to blue on end of pattern',
                   after=ANSI_BACKGROUND_BLUE),
            Filter(name='background-magenta-after',
                   long_option='background-magenta-after',
                   help='toggle background to magenta on end of pattern',
                   after=ANSI_BACKGROUND_MAGENTA),
            Filter(name='background-cyan-after',
                   long_option='background-cyan-after',
                   help='toggle background to cyan on end of pattern',
                   after=ANSI_BACKGROUND_CYAN),
            Filter(name='background-reset-after',
                   long_option='background-reset-after',
                   help='reset background color on end of pattern',
                   after=ANSI_BACKGROUND_RESET),
        ]
    ),
    FilterGroup(
        name='Text effects',
        help='Use these options to associate patterns to text effects.',
        filters=[
            Filter(name='bold',
                   long_option='bold',
                   help='print pattern in bold',
                   before=ANSI_BOLD,
                   after=ANSI_RESET_INTENSITY),
            Filter(name='bold-before',
                   long_option='bold-before',
                   help='toggle bold on beginning of pattern',
                   before=ANSI_BOLD),
            Filter(name='bold-after',
                   long_option='bold-after',
                   help='toggle bold on end of pattern',
                   after=ANSI_BOLD),
            Filter(name='faint',
                   long_option='faint',
                   help='print pattern with decreased intensity',
                   before=ANSI_FAINT,
                   after=ANSI_RESET_INTENSITY),
            Filter(name='faint-before',
                   long_option='faint-before',
                   help='toggle faint on beginning of pattern',
                   before=ANSI_FAINT),
            Filter(name='faint-after',
                   long_option='faint-after',
                   help='toggle faint on end of pattern',
                   after=ANSI_FAINT),
            Filter(name='intensity-reset-before',
                   long_option='intensity-reset-before',
                   help='reset text intensity (bold, faint) on beginning of pattern',
                   before=ANSI_RESET_INTENSITY),
            Filter(name='intensity-reset-after',
                   long_option='intensity-reset-after',
                   help='reset text intensity (bold, faint) on end of pattern',
                   after=ANSI_RESET_INTENSITY),
            Filter(name='italic',
                   long_option='italic',
                   help='print pattern in italic',
                   before=ANSI_ITALIC,
                   after=ANSI_RESET_ITALIC),
            Filter(name='italic-before',
                   long_option='italic-before',
                   help='toggle italic on beginning of pattern',
                   before=ANSI_ITALIC),
            Filter(name='italic-after',
                   long_option='italic-after',
                   help='toggle italic on end of pattern',
                   after=ANSI_ITALIC),
            Filter(name='italic-reset-before',
                   long_option='italic-reset-before',
                   help='reset italic on beginning of pattern',
                   before=ANSI_RESET_ITALIC),
            Filter(name='italic-reset-after',
                   long_option='italic-reset-after',
                   help='reset italic on end of pattern',
                   after=ANSI_RESET_ITALIC),
            Filter(name='underline',
                   long_option='underline',
                   help='print pattern underlined',
                   before=ANSI_UNDERLINE,
                   after=ANSI_RESET_UNDERLINE),
            Filter(name='underline-before',
                   long_option='underline-before',
                   help='toggle underline on beginning of pattern',
                   before=ANSI_UNDERLINE),
            Filter(name='underline-after',
                   long_option='underline-after',
                   help='toggle underline on end of pattern',
                   after=ANSI_UNDERLINE),
            Filter(name='underline-double',
                   long_option='underline-double',
                   help='print pattern double underlined',
                   before=ANSI_UNDERLINE_DOUBLE,
                   after=ANSI_RESET_UNDERLINE),
            Filter(name='underline-double-before',
                   long_option='underline-double-before',
                   help='toggle double underline on beginning of pattern',
                   before=ANSI_UNDERLINE_DOUBLE),
            Filter(name='underline-double-after',
                   long_option='underline-double-after',
                   help='toggle double underline on end of pattern',
                   after=ANSI_UNDERLINE_DOUBLE),
            Filter(name='underline-reset-before',
                   long_option='underline-reset-before',
                   help='reset underline on beginning of pattern',
                   before=ANSI_RESET_UNDERLINE),
            Filter(name='underline-reset-after',
                   long_option='underline-reset-after',
                   help='reset underline on end of pattern',
                   after=ANSI_RESET_UNDERLINE),
            Filter(name='blink',
                   long_option='blink',
                   help='print pattern blinking',
                   before=ANSI_BLINK,
                   after=ANSI_RESET_BLINK),
            Filter(name='blink-before',
                   long_option='blink-before',
                   help='toggle blinking on beginning of pattern',
                   before=ANSI_BLINK),
            Filter(name='blink-after',
                   long_option='blink-after',
                   help='toggle blinking on end of pattern',
                   after=ANSI_BLINK),
            Filter(name='blink-rapid',
                   long_option='blink-rapid',
                   help='print pattern blinking rapidly',
                   before=ANSI_BLINK,
                   after=ANSI_RESET_BLINK),
            Filter(name='blink-rapid-before',
                   long_option='blink-rapid-before',
                   help='toggle rapid blinking on beginning of pattern',
                   before=ANSI_BLINK),
            Filter(name='blink-rapid-after',
                   long_option='blink-rapid-after',
                   help='toggle rapid blinking on end of pattern',
                   after=ANSI_BLINK),
            Filter(name='blink-reset-before',
                   long_option='blink-reset-before',
                   help='reset blinking on beginning of pattern',
                   before=ANSI_RESET_BLINK),
            Filter(name='blink-reset-after',
                   long_option='blink-reset-after',
                   help='reset blinking on end of pattern',
                   after=ANSI_RESET_BLINK),
            Filter(name='negative',
                   long_option='negative',
                   help='print pattern swapping foreground and background',
                   before=ANSI_NEGATIVE,
                   after=ANSI_RESET_NEGATIVE),
            Filter(name='negative-before',
                   long_option='negative-before',
                   help='toggle negative on beginning of pattern',
                   before=ANSI_NEGATIVE),
            Filter(name='negative-after',
                   long_option='negative-after',
                   help='toggle negative on end of pattern',
                   after=ANSI_NEGATIVE),
            Filter(name='negative-reset-before',
                   long_option='negative-reset-before',
                   help='reset negative on beginning of pattern',
                   before=ANSI_RESET_NEGATIVE),
            Filter(name='negative-reset-after',
                   long_option='negative-reset-after',
                   help='reset negative on end of pattern',
                   after=ANSI_RESET_NEGATIVE),
            Filter(name='hide',
                   long_option='hide',
                   help='print pattern hidden',
                   before=ANSI_HIDE,
                   after=ANSI_RESET_HIDE),
            Filter(name='hide-before',
                   long_option='hide-before',
                   help='toggle hiding on beginning of pattern',
                   before=ANSI_HIDE),
            Filter(name='hide-after',
                   long_option='hide-after',
                   help='toggle hiding on end of pattern',
                   after=ANSI_HIDE),
            Filter(name='hide-reset-before',
                   long_option='hide-reset-before',
                   help='reset hiding on beginning of pattern',
                   before=ANSI_RESET_HIDE),
            Filter(name='hide-reset-after',
                   long_option='hide-reset-after',
                   help='reset hiding on end of pattern',
                   after=ANSI_RESET_HIDE),
        ]
    )
]

FILTERS_BY_NAME = {filter.name: filter for group in FILTER_GROUPS for filter in group.filters}
FILTERS_BY_SHORT_OPTION = {filter.short_option: filter for group in FILTER_GROUPS for filter in group.filters}
FILTERS_BY_LONG_OPTION = {filter.long_option: filter for group in FILTER_GROUPS for filter in group.filters}
