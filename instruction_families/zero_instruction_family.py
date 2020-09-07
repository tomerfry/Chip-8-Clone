"""
This module implements the Instruction classes from the zero family.
"""
from instruction import Instruction
from byte_manipulation import *


def handle_zero_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    instruction_value = get_word(top_byte, bottom_byte)
    if instruction_value == CLS_INSTRUCTION:
        return ClsInstruction(raw)
    elif instruction_value == RET_INSTRUCTION:
        return RetInstruction(raw)
    else:
        addr = get_three_last_nibbles(top_byte, bottom_byte)
        return SysInstruction(addr, raw)


class ClsInstruction(Instruction):
    """
    The Clear-screen instruction class.
    """
    def __init__(self, raw):
        super().__init__(raw)

    def affect_chip_state(self, registers, mem, stack, screen):
        """
        This affects the chip state according to the instruction.
        :param Registers registers: The chip registers.
        :param bytearray mem: The chip memory.
        :param list stack: The chip stack.
        :return: None
        """
        screen.clear_screen()
        registers.forward_pc()


class RetInstruction(Instruction):
    """
    The Return instruction class.
    """
    def __init__(self, raw):
        super().__init__(raw)

    def affect_chip_state(self, registers, mem, stack, screen):
        """
        This affects the chip state according to the instruction.
        :param Registers registers: The chip registers.
        :param bytearray mem: The chip memory.
        :param list stack: The chip stack.
        :return: None
        """
        registers.set_pc(stack.pop())


class SysInstruction(Instruction):
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
        print('This instruction is ignored')
        registers.forward_pc()
