"""
This module implements the Instruction classes from the two family.
"""
from byte_manipulation import *


def handle_two_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    addr = get_three_last_nibbles(raw[0], raw[1])
    call_instruction(addr, chip.registers, chip.stack)


def call_instruction(addr, registers, stack):
    """
    Affect the chip registers and memory.
    :param Registers registers: The chip registers
    :param bytearray mem: The chip memory
    :param list stack: The chip stack
    :return: None
    """
    stack.insert(len(stack), registers.next_instruction_addr())
    registers.set_pc(addr)
