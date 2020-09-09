import struct

# Program arguments
from instruction_families.a_instruction_family import handle_a_family

PROGRAM_ARGUMENT = '--program'
DEFAULT_GAME = 'games/pong.ch8'

# Logging
LOG_FILENAME = 'log/chip_8.log'

# CHIP-8
CHIP_8_NAME = 'chip-8'
MEMORY_SIZE = 0x1000
REGISTERS_COUNT = 0x10
INTERPRETER_SIZE = 0x200
STANDARD_ENTRY_POINT = 0x200

# Screen
WIDTH = 64
HEIGHT = 32
TILE_LEN = 10

# Timers
DT_TIME_SPAN = 60 / 1000

# InstructionFactory
FIRST_BYTE_STRUCT = '>BB'
BOTTOM_NIBBLE_MASK = 0x0f
NIBBLE_OFFSET = 4

# Registers

REGISTER_BIT_MASK = 0xff
WORD_REGISTER_BIT_MASK = 0xffff
REGISTER_LEAST_SIG_BIT = 0x1
REGISTER_MOST_SIG_BIT = 2 ** 7

# Instructions
INSTRUCTION_SIZE = 2

# Instruction Family Zero
ZERO_FAMILY_ID = 0
CLS_INSTRUCTION = 0x00e0
RET_INSTRUCTION = 0x00ee

# Instruction Family One
ONE_FAMILY_ID = 1

# Instruction Family Two
TWO_FAMILY_ID = 2

# Instruction Family Two
THREE_FAMILY_ID = 3

# Instruction Family Four
FOUR_FAMILY_ID = 4

# Instruction Family Four
FIVE_FAMILY_ID = 5

# Instruction Family Six
SIX_FAMILY_ID = 6

# Instruction Family Seven
SEVEN_FAMILY_ID = 7

# Instruction Family Eight
EIGHT_FAMILY_ID = 8
EIGHT_OPCODE_BITMASK = 0xf00f
ASSIGN_OPCODE = 0x8000
ASSIGN_BIT_OR_OPCODE = 0x8001
ASSIGN_BIT_AND_OPCODE = 0x8002
ASSIGN_BIT_XOR_OPCODE = 0x8003
ADD_REG_OPCODE = 0x8004
SUB_REG_OPCODE = 0x8005
SHR_REG_OPCODE = 0x8006
SUB_Y_BY_X_OPCODE = 0x8007
SHL_REG_OPCODE = 0x800e

# Instruction Family Nine
NINE_FAMILY_ID = 9

# Instruction Family A
A_FAMILY_ID = 0xa

# Instruction Family B
B_FAMILY_ID = 0xb

# Instruction Family C
C_FAMILY_ID = 0xc

# Instruction Family D
D_FAMILY_ID = 0xd

# Instruction Family E
E_FAMILY_ID = 0xe
E_OPCODE_BITMASK = 0xf0ff
E_KEY_PRESSED_OPCODE = 0xe09e
E_KEY_RELEASED_OPCODE = 0xe0a1

# Instruction Family F
F_FAMILY_ID = 0xf
F_OPCODE_BITMASK = 0xf0ff
F_GET_DT_OPCODE = 0xf007
F_AWAIT_KEY_OPCODE = 0xf00a
F_SET_DT_OPCODE = 0xf015
F_SET_ST_OPCODE = 0xf018
F_ADD_I_OPCODE = 0xf01e
F_I_CHAR_ADDR_OPCODE = 0xf029
F_BCD_OPCODE = 0xf033
F_MEM_DUMP_OPCODE = 0xf055
F_MEM_LOAD_OPCODE = 0xf065


# Fonts
FONTS = [0xf0909090f0, 0x2060202070, 0xf010f080f0, 0xf010f010f0, 0x9090f01010, 0xf080f010f0, 0xf080f090f0, 0xf010204040,
         0xf090f090f0, 0xf090f010f0, 0xf090f09090, 0xe090e090e0, 0xf0808080f0, 0xe0909090e0, 0xf080f080f0, 0xf080f08080]
FONTS_ADDRESSES = {
    0: 0x0,
    1: 5,
    2: 10,
    3: 15,
    4: 20,
    5: 25,
    6: 30,
    7: 35,
    8: 40,
    9: 45,
    0xa: 50,
    0xb: 55,
    0xc: 60,
    0xd: 65,
    0xe: 70,
    0xf: 75
}

FONTS_MEMORY = 0
for font in FONTS:
    FONTS_MEMORY += font
    FONTS_MEMORY = FONTS_MEMORY << (8 * 5)
FONTS_MEMORY_SIZE = 85
FONTS_MEMORY = int.to_bytes(FONTS_MEMORY, FONTS_MEMORY_SIZE, byteorder='big')

INSTRUCTIONS = {
    ZERO_FAMILY_ID: None,
    ONE_FAMILY_ID: None,
    TWO_FAMILY_ID: None,
    THREE_FAMILY_ID: None,
    FOUR_FAMILY_ID: None,
    FIVE_FAMILY_ID: None,
    SIX_FAMILY_ID: None,
    SEVEN_FAMILY_ID: None,
    EIGHT_FAMILY_ID: None,
    NINE_FAMILY_ID: None,
    A_FAMILY_ID: handle_a_family,
    B_FAMILY_ID: None,
    C_FAMILY_ID: None,
    D_FAMILY_ID: None,
    E_FAMILY_ID: None,
    F_FAMILY_ID: None
}

