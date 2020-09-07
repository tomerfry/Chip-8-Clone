"""
Module implements the registers class.
"""
from consts import *


class Registers(object):
    """
    Class to manage the chip registers.
    """
    def __init__(self):
        # The Chip-8 registers
        self.v_registers = [0] * REGISTERS_COUNT
        # The I register
        self.i = 0x0
        # The PC register is the Program-Counter register
        self.pc = 0x0
        # The Delay-Timer register
        self.dt = 0x0
        # The Sound-Timer register
        self.st = 0x0

    def reset(self):
        """
        Reset the registers state.
        """
        self.v_registers = [0] * REGISTERS_COUNT
        self.i = 0x0
        self.pc = STANDARD_ENTRY_POINT
        self.dt = 0x0
        self.st = 0x0

    def is_dt_set(self):
        """
        Is the Delay-Timer register set.
        :return: Return if the Delay-Timer register is set with some value other then 0x0.
        :rtype: bool
        """
        return self.dt > 0x0

    def sub_dt(self):
        """
        Subtract the Delay-Timer register by 1.
        :return: None
        """
        self.dt -= 1

    def set_v_register(self, v_register, value):
        """
        Set the specified v_register.
        :param v_register: The specified v_register.
        :param value: The value to set the register to.
        """
        self.v_registers[v_register] = value & REGISTER_BIT_MASK

    def forward_pc(self):
        """
        Forward the PC register by one instruction.
        """
        self.pc += INSTRUCTION_SIZE

    def skip_pc(self):
        """
        Forward the PC register by 2 instructions.
        """
        self.pc += INSTRUCTION_SIZE * 2

    def set_pc(self, value):
        """
        Set the PC register to the given value.
        :param int value: The given value to set the register.
        :return: None
        """
        self.pc = value & WORD_REGISTER_BIT_MASK

    def set_i(self, value):
        self.i = value & WORD_REGISTER_BIT_MASK

    def next_instruction_addr(self):
        return self.pc + 2

    def __repr__(self):
        state_string = ''
        for register, value in enumerate(self.v_registers):
            state_string += 'V{0:X}: {1}\n'.format(register, value)
        state_string += 'PC: {0}\n'.format(self.pc)
        state_string += 'I: {0}\n'.format(self.i)
        state_string += 'DT: {0}\n'.format(self.dt)
        state_string += 'ST: {0}\n'.format(self.st)
        return state_string

    def set_dt(self, value):
        self.dt = value

    def set_st(self, value):
        self.st = value
