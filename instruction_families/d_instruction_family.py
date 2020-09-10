"""
This module implements the Instruction classes from the D family.
"""
from byte_manipulation import *


def handle_d_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    vx = get_bottom_nibble(raw[0])
    vy = get_top_nibble(raw[1])
    height = get_bottom_nibble(raw[1])
    raw_sprite = chip.mem[chip.registers.i:chip.registers.i + height]
    x = chip.registers.v_registers[vx]
    y = chip.registers.v_registers[vy]
    vf = chip.screen.draw_sprite(x, y, 8, height, raw_sprite)
    chip.registers.set_v_register(0xf, vf)
    chip.registers.forward_pc()