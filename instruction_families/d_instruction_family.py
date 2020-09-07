"""
This module implements the Instruction classes from the D family.
"""
from instruction import Instruction
from byte_manipulation import *


def handle_d_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    vx = get_bottom_nibble(top_byte)
    vy = get_top_nibble(bottom_byte)
    height = get_bottom_nibble(bottom_byte)
    return DrawInstruction(vx, vy, height, raw)


class DrawInstruction(Instruction):
    def __init__(self, v_register_x, v_register_y, height, raw):
        super().__init__(raw)
        self.v_register_x = v_register_x
        self.v_register_y = v_register_y
        self.height = height

    def affect_chip_state(self, registers, mem, stack, screen):
        raw_sprite = mem[registers.i:registers.i + self.height]
        x = registers.v_registers[self.v_register_x]
        y = registers.v_registers[self.v_register_y]
        vf = screen.draw_sprite(x, y, 8, self.height, raw_sprite)
        registers.set_v_register(0xf, vf)
        registers.forward_pc()
