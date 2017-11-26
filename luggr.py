"""
Luggr, a simple, small logging library for Python.

Copyright (c) 2017 S Stewart <iamtheworst@programmer.net>

Licensed under the MIT License.
"""
from colored import fg, bg, attr, stylize

colors = {
    'debug': colored.fg(141) + colored.attr('bold'),
    'info': colored.fg(153) + colored.attr('bold'),
    'warn': colored.fg(226) + colored.attr('bold'),
    'err': colored.fg(196) + colored.attr('bold'),
}

def debug(msg):
    """Prints a logging message as level debug."""
    print(stylize('[DEBUG]', colors['debug']) + msg)

def info(msg):
    """Prints a logging message as level info."""
    print(stylize('[INFO]', colors['info']) + msg)

def warn(msg):
    """Prints a logging message as level warn."""
    print(stylize('[WARNING]', colors['warn']) + msg)

def error(msg):
    """Prints a logging message as level err."""
    print(stylize('[ERROR]', colors['err']) + msg)

def custom(msg, level, color):
    """Prints a logging message at a custom level.
    Arguments:
    - msg: Message to log.
    - level: Level to log as.
    - color: what color to use for the level thing"""
    print(stylize('[{}]'.format(level), colored.fg(color) + colored.attr('bold')) + msg)
