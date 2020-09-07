"""
This module implements the Instruction classes from the E family.
"""
from instruction import Instruction
from byte_manipulation import *
from consts import *


def handle_e_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    instruction_value = get_word(top_byte, bottom_byte) & E_OPCODE_BITMASK
    vx = get_bottom_nibble(top_byte)

    if instruction_value == E_KEY_PRESSED_OPCODE:
        return KeyPressedInstruction(vx, raw)
    elif instruction_value == E_KEY_RELEASED_OPCODE:
        return KeyReleasedInstruction(vx, raw)


class KeyPressedInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        if screen.key_status(registers.v_registers[self.vx]):
            registers.skip_pc()
        else:
            registers.forward_pc()


class KeyReleasedInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        if not screen.key_status(registers.v_registers[self.vx]):
            registers.skip_pc()
        else:
            registers.forward_pc()