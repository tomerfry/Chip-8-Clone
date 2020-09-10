"""
This module implements the Instruction classes from the three family.
"""
from byte_manipulation import *


def handle_three_family(chip, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    vx = get_bottom_nibble(raw[0])
    value = raw[1]
    skip_equal_imm(vx, value, chip.registers)


def skip_equal_imm(vx, value, registers):
    if registers.v_registers[vx] == value:
        registers.skip_pc()
    else:
        registers.forward_pc()