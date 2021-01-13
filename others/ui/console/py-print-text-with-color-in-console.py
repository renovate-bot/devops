#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def _wrap_with(code):
    def inner(text, bold=False):
        c = code

        if os.environ.get('FABRIC_DISABLE_COLORS'):  # or os.name == 'nt':
            return text

        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)

    return inner


red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')
blue = _wrap_with('34')
magenta = _wrap_with('35')
cyan = _wrap_with('36')
white = _wrap_with('37')

if __name__ == '__main__':
    if os.name == 'nt':
        print("not support on Microsoft cmd and powershell")
    print(red("hello world!"))
    print(green("hello world!"))
    print(yellow("hello world!"))
    print(blue("hello world!"))
    print(magenta("hello world!"))
    print(cyan("hello world!"))
    print(white("hello world!"))
