"""
This module implements the Instruction classes from the zero family.
"""
from byte_manipulation import *


def handle_zero_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    instruction_value = get_word(raw[0], raw[1])

    if instruction_value == CLS_INSTRUCTION:
        cls_instruction(chip.registers, chip.screen)
    elif instruction_value == RET_INSTRUCTION:
        ret_instruction(chip.registers, chip.stack)
    else:
        sys_instruction(chip.registers)


def cls_instruction(registers, screen):
    """

    :param Chip8 chip:
    :param registers:
    :param screen:
    :return:
    """
    screen.clear_screen()
    registers.forward_pc()


def ret_instruction(registers, stack):
    """
    This affects the chip state according to the instruction.
    :param Registers registers: The chip registers.
    :param bytearray mem: The chip memory.
    :param list stack: The chip stack.
    :return: None
    """
    registers.set_pc(stack.pop())


def sys_instruction(registers):
    """
    Affect the chip registers and memory.
    :param Registers registers: The chip registers
    :param bytearray mem: The chip memory
    :param list stack: The chip stack
    :return: None
    """
    print('This instruction is ignored')
    registers.forward_pc()
