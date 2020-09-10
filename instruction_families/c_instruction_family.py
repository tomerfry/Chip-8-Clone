"""
This module implements the Instruction classes from the C family.
"""
import random

from byte_manipulation import *


def handle_c_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    v_register = get_bottom_nibble(raw[0])
    value = raw[1]
    chip.registers.set_v_register(v_register, random.randint(0, 0xff) & value)
    chip.registers.forward_pc()