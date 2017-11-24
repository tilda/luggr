"""
Luggr, a simple, small logging library for Python.

Copyright (c) 2017 S Stewart <iamtheworst@programmer.net>

Licensed under the MIT License.
"""
import colored

colors = {
    'debug': colored.fg(141) + colored.attr('bold'),
    'info': colored.fg(153) + colored.attr('bold'),
    'warn': colored.fg(226) + colored.attr('bold'),
    'err': colored.fg(196) + colored.attr('bold'),
    'reset': colored.attr('reset')
}

def debug(msg):
    print(colors['debug'] + ''.format(msg) + colors['reset'])

def info(msg):
    print(colors['info'] + ''.format(msg) + colors['reset'])

def warn(msg):
    print(colors['warn'] + ''.format(msg) + colors['reset'])

def err(msg):
    print(colors['err'] + ''.format(msg) + colors['reset'])
