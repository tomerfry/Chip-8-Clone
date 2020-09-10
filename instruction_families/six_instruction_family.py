"""
This module implements the Instruction classes from the six family.
"""
from byte_manipulation import *


def handle_six_family(chip, raw):
    """
    This function is used in instruction resolution.
    :param int top_byte: The top-byte of the instruction.
    :param int bottom_byte: The bottom-byte of the instruction.
    :param bytearray raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    vx = get_bottom_nibble(raw[0])
    value = raw[1]
    set_instruction(vx, value, chip.registers)


def set_instruction(vx, value, registers):
    """
    Affect the chip registers and memory.
    :param Registers registers: The chip registers
    :param bytearray mem: The chip memory
    :param list stack: The chip stack
    :return: None
    """
    registers.v_registers[vx] = value
    registers.forward_pc()
