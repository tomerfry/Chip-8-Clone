"""
This module implements the Instruction classes from the two family.
"""
from instruction import Instruction
from byte_manipulation import *


def handle_two_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    addr = get_three_last_nibbles(top_byte, bottom_byte)
    return CallInstruction(addr, raw)


class CallInstruction(Instruction):
    """
    The SysInstruction class.
    """

    def __init__(self, addr, raw):
        """
        :param int addr: The call address destination.
        :param bytearray raw: The raw bytes of the instruction.
        """
        super().__init__(raw)
        self.addr = addr

    def affect_chip_state(self, registers, mem, stack, screen):
        """
        Affect the chip registers and memory.
        :param Registers registers: The chip registers
        :param bytearray mem: The chip memory
        :param list stack: The chip stack
        :return: None
        """
        stack.insert(len(stack), registers.next_instruction_addr())
        registers.set_pc(self.addr)
