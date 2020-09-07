"""
This module implements the Instruction classes from the B family.
"""
from instruction import Instruction
from byte_manipulation import *


def handle_b_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    return JumpInstruction(get_three_last_nibbles(top_byte, bottom_byte), raw)


class JumpInstruction(Instruction):
    def __init__(self, addr, raw):
        super().__init__(raw)
        self.addr = addr

    def affect_chip_state(self, registers, mem, stack, screen):
        registers.set_pc(registers.v_registers[0x0] + self.addr)