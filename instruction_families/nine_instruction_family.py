"""
This module implements the Instruction classes from the nine family.
"""
from byte_manipulation import *


def handle_nine_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    vx = get_bottom_nibble(raw[0])
    vy = get_top_nibble(raw[1])
    skip_not_equal_reg(vx, vy, chip.registers)


def skip_not_equal_reg(vx, vy, registers):
    if registers.v_registers[vx] != registers.v_registers[vy]:
        registers.skip_pc()
    else:
        registers.forward_pc()
