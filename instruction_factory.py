"""
This module implements the Instruction-Factory .
"""
import struct

from byte_manipulation import *
from instruction_families.zero_instruction_family import handle_zero_family
from instruction_families.one_instruction_family import handle_one_family
from instruction_families.two_instruction_family import handle_two_family
from instruction_families.three_instruction_family import handle_three_family
from instruction_families.four_instruction_family import handle_four_family
from instruction_families.five_instruction_family import handle_five_family
from instruction_families.six_instruction_family import handle_six_family
from instruction_families.seven_instruction_family import handle_seven_family
from instruction_families.eight_instruction_family import handle_eight_family
from instruction_families.nine_instruction_family import handle_nine_family
from instruction_families.a_instruction_family import handle_a_family
from instruction_families.b_instruction_family import handle_b_family
from instruction_families.c_instruction_family import handle_c_family
from instruction_families.d_instruction_family import handle_d_family
from instruction_families.e_instruction_family import handle_e_family
from instruction_families.f_instruction_family import handle_f_family



# A dict holding handler functions for each instruction family.
# Based on the first nibble of the raw instruction.
INSTRUCTIONS = {
    ZERO_FAMILY_ID: handle_zero_family,
    ONE_FAMILY_ID: handle_one_family,
    TWO_FAMILY_ID: handle_two_family,
    THREE_FAMILY_ID: handle_three_family,
    FOUR_FAMILY_ID: handle_four_family,
    FIVE_FAMILY_ID: handle_five_family,
    SIX_FAMILY_ID: handle_six_family,
    SEVEN_FAMILY_ID: handle_seven_family,
    EIGHT_FAMILY_ID: handle_eight_family,
    NINE_FAMILY_ID: handle_nine_family,
    A_FAMILY_ID: handle_a_family,
    B_FAMILY_ID: handle_b_family,
    C_FAMILY_ID: handle_c_family,
    D_FAMILY_ID: handle_d_family,
    E_FAMILY_ID: handle_e_family,
    F_FAMILY_ID: handle_f_family
}


def get_from_raw(raw):
    """
    Return an instruction instance
    :param raw: The raw instruction bytes.
    :return: A specific instance of an instruction.
    :rtype: Instruction
    """
    top_byte, bottom_byte = struct.unpack(FIRST_BYTE_STRUCT, raw)
    top_nibble = get_top_nibble(top_byte)
    if top_nibble not in INSTRUCTIONS:
        raise Exception('Unknown instruction: {}'.format(raw))
    instruction_instance = INSTRUCTIONS[top_nibble](top_byte, bottom_byte, raw)
    return instruction_instance
