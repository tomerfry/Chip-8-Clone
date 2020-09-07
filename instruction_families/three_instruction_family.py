"""
This module implements the Instruction classes from the three family.
"""
from instruction import Instruction
from byte_manipulation import *


def handle_three_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    vx = get_bottom_nibble(top_byte)
    value = bottom_byte
    return SkipEqualImm(vx, value, raw)


class SkipEqualImm(Instruction):
    def __init__(self, vx, value, raw):
        super().__init__(raw)
        self.vx = vx
        self.value = value

    def affect_chip_state(self, registers, mem, stack, screen):
        if registers.v_registers[self.vx] == self.value:
            registers.skip_pc()
        else:
            registers.forward_pc()