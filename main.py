#! /usr/bin/python3

import argparse
import logging
import sys
import threading

from consts import *
from chip import Chip8
from screen import Screen


def setup_logging():
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, filemode='w')
    logger = logging.getLogger('main')
    logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    return logger


def parse_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument(PROGRAM_ARGUMENT, type=str, default=DEFAULT_GAME)
    return args_parser.parse_args()


def main():
    logger = setup_logging()
    logger.info('The Chip-8 Clone VM of Tomer. * Inspired by gynvael')

    args = parse_args()

    screen = Screen()
    screen.start()

    vm = Chip8(screen)
    vm.start_chip(args.program)
    logger.debug('Started the chip.')


if __name__ == '__main__':
    main()