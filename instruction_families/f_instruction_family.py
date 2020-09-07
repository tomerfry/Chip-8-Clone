"""
This module implements the Instruction classes from the F family.
"""
from instruction import Instruction
from byte_manipulation import *
from consts import *


def handle_f_family(top_byte, bottom_byte, raw):
    """
    This function is used in instruction resolution.
    :param top_byte: The top-byte of the instruction.
    :param bottom_byte: The bottom-byte of the instruction.
    :param raw: The raw instruction.
    :return: The instruction instance.
    :rtype: Instruction
    """
    instruction_value = get_word(top_byte, bottom_byte) & F_OPCODE_BITMASK
    vx = get_bottom_nibble(top_byte)
    if instruction_value == F_GET_DT_OPCODE:
        return GetDTInstruction(vx, raw)
    elif instruction_value == F_AWAIT_KEY_OPCODE:
        return AwaitKeyInstruction(vx, raw)
    elif instruction_value == F_SET_DT_OPCODE:
        return SetDTInstruction(vx, raw)
    elif instruction_value == F_SET_ST_OPCODE:
        return SetSTInstruction(vx, raw)
    elif instruction_value == F_ADD_I_OPCODE:
        return AddIInstruction(vx, raw)
    elif instruction_value == F_I_CHAR_ADDR_OPCODE:
        return SetICharAddrInstruction(vx, raw)
    elif instruction_value == F_BCD_OPCODE:
        return BCDInstruction(vx, raw)
    elif instruction_value == F_MEM_DUMP_OPCODE:
        return MemDumpInstruction(vx, raw)
    elif instruction_value == F_MEM_LOAD_OPCODE:
        return MemLoadInstruction(vx, raw)


class GetDTInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        registers.set_v_register(self.vx, registers.dt)
        registers.forward_pc()


class AwaitKeyInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        pressed_key = screen.await_key()
        registers.set_v_register(self.vx, pressed_key)
        registers.forward_pc()


class SetDTInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        registers.set_dt(registers.v_registers[self.vx])
        registers.forward_pc()


class SetSTInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        registers.set_st(registers.v_registers[self.vx])
        registers.forward_pc()


class AddIInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        registers.set_i(registers.i + registers.v_registers[self.vx])
        registers.forward_pc()


class SetICharAddrInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        registers.set_i(FONTS_ADDRESSES[registers.v_registers[self.vx]])
        registers.forward_pc()


class BCDInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        value = registers.v_registers[self.vx]
        ones = value % 10
        value //= 10
        tens = value % 10
        value //= 10
        hundreds = value % 10
        mem[registers.i] = hundreds
        mem[registers.i + 1] = tens
        mem[registers.i + 2] = ones
        registers.forward_pc()


class MemDumpInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        for i in range(self.vx):
            mem[registers.i + i] = registers.v_registers[i]
        registers.forward_pc()


class MemLoadInstruction(Instruction):
    def __init__(self, vx, raw):
        super().__init__(raw)
        self.vx = vx

    def affect_chip_state(self, registers, mem, stack, screen):
        for i in range(self.vx):
            registers.set_v_register(i, mem[registers.i + i])
        registers.forward_pc()