"""
This module implements the Instruction classes from the A family.
"""
from byte_manipulation import *


def handle_a_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    addr = get_three_last_nibbles(raw[0], raw[1])
    chip.registers.set_i(addr)
    chip.registers.forward_pc()
