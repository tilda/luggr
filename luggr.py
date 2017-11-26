"""
Luggr, a simple, small logging library for Python.

Copyright (c) 2017 S Stewart <iamtheworst@programmer.net>

Licensed under the MIT License.
"""
from colored import fg, bg, attr, stylize

colors = {
    'debug': fg(141) + attr('bold'),
    'info': fg(153) + attr('bold'),
    'warn': fg(226) + attr('bold'),
    'err': fg(196) + attr('bold'),
}

def debug(msg):
    """Prints a logging message as level debug."""
    print(stylize('[DEBUG]', colors['debug']) + ' {}'.format(msg))

def info(msg):
    """Prints a logging message as level info."""
    print(stylize('[INFO]', colors['info']) + ' {}'.format(msg))

def warn(msg):
    """Prints a logging message as level warn."""
    print(stylize('[WARNING]', colors['warn']) + ' {}'.format(msg))

def error(msg):
    """Prints a logging message as level err."""
    print(stylize('[ERROR]', colors['err']) + ' {}'.format(msg))

def custom(msg, level, color):
    """Prints a logging message at a custom level.
    Arguments:
    - msg: Message to log.
    - level: Level to log as.
    - color: what color to use for the level thing"""
    print(stylize('[{}]'.format(level), fg(color) + attr('bold')) + ' {}'.format(msg))
