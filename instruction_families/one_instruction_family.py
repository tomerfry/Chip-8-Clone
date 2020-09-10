"""
This module implements the Instruction classes from the one family.
"""
from byte_manipulation import *


def handle_one_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    addr = get_three_last_nibbles(raw[0], raw[1])
    goto_instruction(addr, chip.registers)


def goto_instruction(addr, registers):
    """
    Affect the chip registers and memory.
    :param Registers registers: The chip registers
    :param bytearray mem: The chip memory
    :param list stack: The chip stack
    :return: None
    """
    registers.set_pc(addr)
