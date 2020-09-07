"""
This module implements the Instruction classes from the six family.
"""
from instruction import Instruction
from byte_manipulation import *


def handle_six_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param int top_byte: The top-byte of the instruction.
    :param int bottom_byte: The bottom-byte of the instruction.
    :param bytearray raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    v_register = get_bottom_nibble(top_byte)
    value = bottom_byte
    return SetInstruction(v_register, value, raw)


class SetInstruction(Instruction):
    """
    The SetInstruction class.
    """
    def __init__(self, v_register, value, raw):
        """
        :param int v_register: The register specified in the instruction.
        :param int value: The value to set the register to.
        :param bytearray raw: The raw bytes of the instruction.
        """
        super().__init__(raw)
        self.v_register = v_register
        self.value = value

    def affect_chip_state(self, registers, mem, stack, screen):
        """
        Affect the chip registers and memory.
        :param Registers registers: The chip registers
        :param bytearray mem: The chip memory
        :param list stack: The chip stack
        :return: None
        """
        registers.set_v_register(self.v_register, self.value)
        registers.forward_pc()
