"""
This module implements the Instruction classes from the seven family.
"""
from byte_manipulation import *


def handle_seven_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    vx = get_bottom_nibble(raw[0])
    value = raw[1]
    add_imm_instruction(vx, value, chip.registers)


def add_imm_instruction(vx, value, registers):
    """
    Affect the chip registers and memory.
    :param Registers registers: The chip registers
    :param bytearray mem: The chip memory
    :param list stack: The chip stack
    :return: None
    """
    registers.v_registers[vx] = (registers.v_registers[vx] + value) & 0xff
    registers.forward_pc()
