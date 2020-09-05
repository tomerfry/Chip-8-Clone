"""
Module defining the CHIP-8 class.
"""
import logging

from consts import *


class Chip8(object):
    """
    The Chip-8 class.
    """
    def __init__(self, screen):
        self.logger = None
        self.setup_logging()
        # The memory
        self.mem = [0] * MEMORY_SIZE
        # The Chip-8 registers
        self.registers = [0] * REGISTERS_COUNT
        # The I register
        self.i = 0x0
        # The PC register is the Program-Counter register
        self.pc = 0x0
        self.screen = screen

    def setup_logging(self):
        self.logger = logging.getLogger(CHIP_8_NAME)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug('Chip-8 class logger initiated.')

    def load_interpreter(self):
        """
        This will load the interpreter section into the memory.
        """
        self.mem[:INTERPRETER_SIZE] = [0] * INTERPRETER_SIZE
        self.logger.debug('Loaded interpreter into memory.')

    def read_memory_image(self, fname):
        """
        Read the memory image from a given file.
        :param str fname: The file name from which to load the memory image.
        :return: None
        """
        with open(fname, 'rb') as f:
            self.mem[INTERPRETER_SIZE:] = list(f.read())
        self.logger.debug('Read memory image from file {}'.format(fname))

    def reset(self):
        """
        This resets the Chip-8.
        The PC register resets to the entry point of the program.
        The registers resets to the value 0x0.
        The memory resets to values of 0x0.
        *Note That the standard entry-point is at address 0x200 (512).
        :return: None
        """
        self.pc = STANDARD_ENTRY_POINT
        self.registers = [0x0] * REGISTERS_COUNT
        self.i = [0x0]
        self.mem = [0x0] * MEMORY_SIZE
        self.logger.debug('Reset the Chip-8')




