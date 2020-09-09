"""
This module implements the Instruction classes from the E family.
"""
from byte_manipulation import *
from consts import *
from chip import Chip8


def handle_e_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    instruction_value = get_word(raw[0], raw[1]) & E_OPCODE_BITMASK
    vx = get_bottom_nibble(raw[0])

    if instruction_value == E_KEY_PRESSED_OPCODE:
        key_pressed_instruction(vx, chip.registers, chip.screen)
    elif instruction_value == E_KEY_RELEASED_OPCODE:
        key_released_instruction(vx, chip.registers, chip.screen)


def key_pressed_instruction(vx, registers, screen):
    if screen.key_status(registers.v_registers[vx]):
        registers.skip_pc()
    else:
        registers.forward_pc()


def key_released_instruction(vx, registers, screen):
    if not screen.key_status(registers.v_registers[vx]):
        registers.skip_pc()
    else:
        registers.forward_pc()
