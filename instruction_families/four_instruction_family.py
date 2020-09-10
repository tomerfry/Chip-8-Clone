"""
This module implements the Instruction classes from the four family.
"""
from byte_manipulation import *


def handle_four_family(chip, raw):
    """

    :param Chip* chip:
    :param raw:
    :return:
    """
    vx = get_bottom_nibble(raw[0])
    value = raw[1]
    skip_not_equal_imm(vx, value, chip.registers)


def skip_not_equal_imm(vx, value, registers):
    if registers.v_registers[vx] != value:
        registers.skip_pc()
    else:
        registers.forward_pc()
