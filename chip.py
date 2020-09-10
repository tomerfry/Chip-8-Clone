"""
Module defining the CHIP-8 class.
"""
import logging
import threading
import time

from instruction_handlers import INSTRUCTIONS
from byte_manipulation import *
from registers import Registers


def setup_chip_logging():
    """
    Setup the chip logger.
    :return: The logger.
    :rtype: logging.Logger
    """
    logger = logging.getLogger(CHIP_8_NAME)
    logger.setLevel(logging.DEBUG)
    return logger


class Chip8():
    """
    The Chip-8 class.
    """

    def __init__(self, screen):
        super().__init__()
        self.logger = setup_chip_logging()
        self.registers = Registers()
        self.mem = bytearray(MEMORY_SIZE)
        self.stack = []
        self.screen = screen
        self.is_processing = False

    def load_fonts(self):
        self.mem[:FONTS_MEMORY_SIZE] = FONTS_MEMORY

    def load_interpreter(self):
        """
        This will load the interpreter section into the memory.
        """
        self.mem[:INTERPRETER_SIZE] = bytearray(INTERPRETER_SIZE)
        self.logger.debug('Loaded interpreter into memory.')

    def read_memory_image(self, fname):
        """
        Read the memory image from a given file.
        :param str fname: The file name from which to load the memory image.
        :return: None
        """
        with open(fname, 'rb') as f:
            self.mem[INTERPRETER_SIZE:] = f.read()
        self.logger.debug('Read memory image from file {}'.format(fname))

    def reset(self):
        """
        This resets the Chip-8.
        The PC register resets to the entry point of the program.
        The registers resets to the value 0x0.
        The memory resets to values of 0x0.
        * Note That the standard entry-point is at address 0x200 (512).
        :return: None
        """
        self.mem = bytearray(MEMORY_SIZE)
        self.load_fonts()
        self.stack = []
        self.registers.reset()
        self.logger.debug('Reset the Chip-8')

    def process_instruction(self):
        pc = self.registers.pc
        raw_instruction = self.mem[pc:pc+2]

        instruction_handler = INSTRUCTIONS[get_top_nibble(raw_instruction[0])]
        instruction_handler(self, raw_instruction)

    def processing(self):
        self.is_processing = True
        last_time = time.time_ns()

        while self.is_processing and self.screen.is_screen_on:
            current_time = time.time_ns()
            if current_time - last_time >= DT_TIME_SPAN:
                last_time = current_time
                if self.registers.is_dt_set():
                    self.registers.sub_dt()
            self.process_instruction()

    def start_chip(self, program):
        self.reset()
        self.logger.debug('Reset the chip')
        self.load_interpreter()
        self.logger.debug('Load the interpreter')
        self.read_memory_image(program)
        self.logger.debug('Read memory image')

        self.processing()
