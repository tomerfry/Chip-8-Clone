"""
This module implements the Instruction classes from the B family.
"""
from instruction import Instruction
from byte_manipulation import *
from chip import Chip8


def handle_b_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    addr = get_three_last_nibbles(raw[0], raw[1])
    chip.registers.set_pc(chip.registers.v_registers[0x0] + addr)