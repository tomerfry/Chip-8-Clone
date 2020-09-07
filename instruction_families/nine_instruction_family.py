"""
This module implements the Instruction classes from the nine family.
"""
from instruction import Instruction
from byte_manipulation import *


def handle_nine_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    vx = get_bottom_nibble(top_byte)
    vy = get_top_nibble(bottom_byte)
    return SkipNotEqualReg(vx, vy, raw)


class SkipNotEqualReg(Instruction):
    def __init__(self, vx, vy, raw):
        super().__init__(raw)
        self.vx = vx
        self.vy = vy

    def affect_chip_state(self, registers, mem, stack, screen):
        if registers.v_registers[self.vx] != registers.v_registers[self.vy]:
            registers.skip_pc()
        else:
            registers.forward_pc()
