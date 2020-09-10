"""
This module implements the Instruction classes from the F family.
"""
from byte_manipulation import *
from consts import *


def handle_f_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    instruction_value = get_word(raw[0], raw[1]) & F_OPCODE_BITMASK
    vx = get_bottom_nibble(raw[0])
    if instruction_value == F_GET_DT_OPCODE:
        get_dt_instruction(vx, chip.registers)
    elif instruction_value == F_AWAIT_KEY_OPCODE:
        await_key_instruction(vx, chip.registers, chip.screen)
    elif instruction_value == F_SET_DT_OPCODE:
        set_dt_instruction(vx, chip.registers)
    elif instruction_value == F_SET_ST_OPCODE:
        set_st_instruction(vx, chip.registers)
    elif instruction_value == F_ADD_I_OPCODE:
        add_i_instruction(vx, chip.registers)
    elif instruction_value == F_I_CHAR_ADDR_OPCODE:
        set_i_char_addr_instruction(vx, chip.registers)
    elif instruction_value == F_BCD_OPCODE:
        bcd_instruction(vx, chip.registers, chip.mem)
    elif instruction_value == F_MEM_DUMP_OPCODE:
        mem_dump_instruction(vx, chip.registers, chip.mem)
    elif instruction_value == F_MEM_LOAD_OPCODE:
        mem_load_instruction(vx, chip.registers, chip.mem)


def get_dt_instruction(vx, registers):
    registers.set_v_register(vx, registers.dt)
    registers.forward_pc()


def await_key_instruction(vx, registers, screen):
    pressed_key = screen.await_key()
    registers.set_v_register(vx, pressed_key)
    registers.forward_pc()


def set_dt_instruction(vx, registers):
    registers.set_dt(registers.v_registers[vx])
    registers.forward_pc()


def set_st_instruction(vx, registers):
    registers.set_st(registers.v_registers[vx])
    registers.forward_pc()


def add_i_instruction(vx, registers):
    registers.set_i(registers.i + registers.v_registers[vx])
    registers.forward_pc()


def set_i_char_addr_instruction(vx, registers):
    registers.set_i(FONTS_ADDRESSES[registers.v_registers[vx]])
    registers.forward_pc()


def bcd_instruction(vx, registers, mem):
    value = registers.v_registers[vx]
    ones = value % 10
    value //= 10
    tens = value % 10
    value //= 10
    hundreds = value % 10
    mem[registers.i] = hundreds
    mem[registers.i + 1] = tens
    mem[registers.i + 2] = ones
    registers.forward_pc()


def mem_dump_instruction(vx, registers, mem):
    for vr in range(vx + 1):
        mem[registers.i + vr] = registers.v_registers[vr]
    registers.forward_pc()


def mem_load_instruction(vx, registers, mem):
    for i in range(vx + 1):
        registers.set_v_register(i, mem[registers.i + i])
    registers.forward_pc()