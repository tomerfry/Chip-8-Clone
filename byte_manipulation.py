"""
A module for byte manipulation functions.
"""
from consts import *


def get_top_nibble(byte):
    """
    Return the top nibble out of a byte.
    BYTE == NN
            ^
    :param byte: The given byte value.
    :return: The top nibble value.
    :rtype: int
    """
    return (byte >> NIBBLE_OFFSET) & BOTTOM_NIBBLE_MASK


def get_bottom_nibble(byte):
    """
    Return the bottom nibble out of a byte.
    BYTE == NN
             ^
    :param byte: The given byte value.
    :return: The bottom nibble value.
    :rtype: int
    """
    return byte & BOTTOM_NIBBLE_MASK


def get_word(top_byte, bottom_byte):
    return (top_byte << 8) + bottom_byte


def get_three_last_nibbles(top_byte, bottom_byte):
    return get_word(top_byte, bottom_byte) & 0xfff
