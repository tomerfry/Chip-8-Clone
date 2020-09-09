"""
This module implements the Instruction classes from the eight family.
"""
from instruction import Instruction
from consts import *
from byte_manipulation import *


def handle_eight_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    instruction_value = get_word(top_byte, bottom_byte)
    instruction_opcode = instruction_value & EIGHT_OPCODE_BITMASK
    vx = get_bottom_nibble(top_byte)
    vy = get_top_nibble(bottom_byte)
    if instruction_opcode == ASSIGN_OPCODE:
        return AssignInstruction(vx, vy, raw)
    elif instruction_opcode == ASSIGN_BIT_OR_OPCODE:
        return AssignBitOrInstruction(vx, vy, raw)
    elif instruction_opcode == ASSIGN_BIT_AND_OPCODE:
        return AssignBitAndInstruction(vx, vy, raw)
    elif instruction_opcode == ASSIGN_BIT_XOR_OPCODE:
        return AssignBitXorInstruction(vx, vy, raw)
    elif instruction_opcode == ADD_REG_OPCODE:
        return AddRegInstruction(vx, vy, raw)
    elif instruction_opcode == SUB_REG_OPCODE:
        return SubRegInstruction(vx, vy, raw)
    elif instruction_opcode == SHR_REG_OPCODE:
        return ShrInstruction(vx, vy, raw)
    elif instruction_opcode == SUB_Y_BY_X_OPCODE:
        return SubYByXInstruction(vx, vy, raw)
    elif instruction_opcode == SHL_REG_OPCODE:
        return ShlInstruction(vx, vy, raw)


def AssignInstruction(self, registers, mem, stack, screen):
    registers.set_v_register(self.vx, registers.v_registers[self.vy])
    registers.forward_pc()


def AssignBitOrInstruction(self, registers, mem, stack, screen):
    value = registers.v_registers[self.vx] | registers.v_registers[self.vy]
    registers.set_v_register(self.vx, value)
    registers.forward_pc()


def AssignBitAndInstruction(self, registers, mem, stack, screen):
    value = registers.v_registers[self.vx] & registers.v_registers[self.vy]
    registers.set_v_register(self.vx, value)
    registers.forward_pc()


def AssignBitXorInstruction(self, registers, mem, stack, screen):
    value = registers.v_registers[self.vx] ^ registers.v_registers[self.vy]
    registers.set_v_register(self.vx, value)
    registers.forward_pc()


def AddRegInstruction(self, registers, mem, stack, screen):
    value = registers.v_registers[self.vx] + registers.v_registers[self.vy]
    if value > 0xff:
        registers.set_v_register(0xf, 1)
    else:
        registers.set_v_register(0xf, 0)
    registers.set_v_register(self.vx, value)
    registers.forward_pc()


def SubRegInstruction(self, registers, mem, stack, screen):
    value = registers.v_registers[self.vx] - registers.v_registers[self.vy]
    registers.set_v_register(self.vx, value & 0xff)
    if value < 0:
        registers.set_v_register(0xf, 1)
    else:
        registers.set_v_register(0xf, 0)
    registers.forward_pc()


def ShrInstruction(self, registers, mem, stack, screen):
    value = registers.v_registers[self.vx] >> 0x1
    registers.set_v_register(0xf, registers.v_registers[self.vx] & REGISTER_LEAST_SIG_BIT)
    registers.set_v_register(self.vx, value)
    registers.forward_pc()


def SubYByXInstruction(self, registers, mem, stack, screen):
    value = registers.v_registers[self.vy] - registers.v_registers[self.vx]
    registers.set_v_register(self.vx, value & 0xff)
    if value < 0:
        registers.set_v_register(0xf, 1)
    else:
        registers.set_v_register(0xf, 0)
    registers.forward_pc()


def ShlInstruction(self, registers, mem, stack, screen):
    value = (registers.v_registers[self.vx] << 0x1) & REGISTER_BIT_MASK
    registers.set_v_register(0xf, registers.v_registers[self.vx] & REGISTER_MOST_SIG_BIT)
    registers.set_v_register(self.vx, value)
    registers.forward_pc()



