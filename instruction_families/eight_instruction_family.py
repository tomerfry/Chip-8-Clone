"""
This module implements the Instruction classes from the eight family.
"""
from byte_manipulation import *


def handle_eight_family(chip, raw):
    """

    :param Chip8 chip:
    :param raw:
    :return:
    """
    instruction_value = get_word(raw[0], raw[1])
    instruction_opcode = instruction_value & EIGHT_OPCODE_BITMASK
    vx = get_bottom_nibble(raw[0])
    vy = get_top_nibble(raw[1])
    if instruction_opcode == ASSIGN_OPCODE:
        assign_instruction(vx, vy, chip.registers)
    elif instruction_opcode == ASSIGN_BIT_OR_OPCODE:
        assign_bit_or_instruction(vx, vy, chip.registers)
    elif instruction_opcode == ASSIGN_BIT_AND_OPCODE:
        assign_bit_and_instruction(vx, vy, chip.registers)
    elif instruction_opcode == ASSIGN_BIT_XOR_OPCODE:
        assign_bit_xor_instruction(vx, vy, chip.registers)
    elif instruction_opcode == ADD_REG_OPCODE:
        add_reg_instruction(vx, vy, chip.registers)
    elif instruction_opcode == SUB_REG_OPCODE:
        sub_reg_instruction(vx, vy, chip.registers)
    elif instruction_opcode == SHR_REG_OPCODE:
        shr_instruction(vx, vy, chip.registers)
    elif instruction_opcode == SUB_Y_BY_X_OPCODE:
        sub_y_by_xinstruction(vx, vy, chip.registers)
    elif instruction_opcode == SHL_REG_OPCODE:
        shl_instruction(vx, vy, chip.registers)


def assign_instruction(vx, vy, registers):
    registers.set_v_register(vx, registers.v_registers[vy])
    registers.forward_pc()


def assign_bit_or_instruction(vx, vy, registers):
    value = registers.v_registers[vx] | registers.v_registers[vy]
    registers.set_v_register(vx, value)
    registers.forward_pc()


def assign_bit_and_instruction(vx, vy, registers):
    value = registers.v_registers[vx] & registers.v_registers[vy]
    registers.set_v_register(vx, value)
    registers.forward_pc()


def assign_bit_xor_instruction(vx, vy, registers):
    value = registers.v_registers[vx] ^ registers.v_registers[vy]
    registers.set_v_register(vx, value)
    registers.forward_pc()


def add_reg_instruction(vx, vy, registers):
    value = (registers.v_registers[vx] + registers.v_registers[vy]) & 0xff
    if value > 0xff:
        registers.set_v_register(0xf, 1)
    else:
        registers.set_v_register(0xf, 0)
    registers.set_v_register(vx, value)
    registers.forward_pc()


def sub_reg_instruction(vx, vy, registers):
    value = (registers.v_registers[vx] - registers.v_registers[vy]) & 0xff
    registers.set_v_register(vx, value & 0xff)
    if registers.v_registers[vx] < registers.v_registers[vy]:
        registers.set_v_register(0xf, 1)
    else:
        registers.set_v_register(0xf, 0)
    registers.forward_pc()


def shr_instruction(vx, vy, registers):
    value = registers.v_registers[vx] >> 0x1
    registers.set_v_register(0xf, registers.v_registers[vx] & REGISTER_LEAST_SIG_BIT)
    registers.set_v_register(vx, value)
    registers.forward_pc()


def sub_y_by_xinstruction(vx, vy, registers):
    value = (registers.v_registers[vy] - registers.v_registers[vx]) & 0xff
    registers.set_v_register(vx, value)
    if registers.v_registers[vy] < registers.v_registers[vx]:
        registers.set_v_register(0xf, 1)
    else:
        registers.set_v_register(0xf, 0)
    registers.forward_pc()


def shl_instruction(vx, vy, registers):
    value = (registers.v_registers[vx] << 0x1) & 0xff
    registers.set_v_register(0xf, registers.v_registers[vx] & REGISTER_MOST_SIG_BIT)
    registers.set_v_register(vx, value)
    registers.forward_pc()



