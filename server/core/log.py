#!/usr/bin/env python3

"""
Copyright (c) 2017 developers (http://r4m80mrx.github.io/)
"""
import logging
import os
import ctypes

# CMD字体颜色
FOREGROUND_BLACK = 0x00
FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x0b
FOREGROUND_GREEN = 0x0a
FOREGROUND_RED = 0x0c
FOREGROUND_YELLOW = 0x0e

# CMD背景颜色
BACKGROUND_WHITE = 0xf0
BACKGROUND_RED = 0xc0
BACKGROUND_SKYBLUE = 0xb0

STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


def reset_color(handle=std_out_handle):
    set_color(FOREGROUND_WHITE)


class Logger:
    def __init__(self, path, clevel=logging.DEBUG, flevel=logging.WARN):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt1 = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(message)s', '%H:%M:%S')
        fmt2 = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt1)
        sh.setLevel(clevel)
        # 文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt2)
        fh.setLevel(flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message, color=FOREGROUND_BLUE):
        set_color(color)
        self.logger.debug(message)
        reset_color()

    def info(self, message, color=FOREGROUND_GREEN):
        set_color(color)
        self.logger.info(message)
        reset_color()

    def warn(self, message, color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)
        reset_color()

    def error(self, message, color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        reset_color()

    def critical(self, message, color=FOREGROUND_BLACK | BACKGROUND_WHITE):
        set_color(color)
        self.logger.critical(message)
        reset_color()

LOGGER = Logger('test.log')

# if __name__ == '__main__':
#     mylog = Logger('test.log')
#     mylog.debug('一个debug信息')
#     mylog.info('一个info信息')
#     mylog.warn('一个warning信息')
#     mylog.error('一个error信息')
#     mylog.critical('一个致命critical信息')
