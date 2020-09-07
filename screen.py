"""
This module implements the screen class.
"""
import pygame
import numpy
import threading

from consts import *

KP_TRANSLATION_MAP = {
    pygame.K_KP0: 0,
    pygame.K_KP1: 1,
    pygame.K_KP2: 2,
    pygame.K_KP3: 3,
    pygame.K_KP4: 4,
    pygame.K_KP5: 5,
    pygame.K_KP6: 6,
    pygame.K_KP7: 7,
    pygame.K_KP8: 8,
    pygame.K_KP9: 9,
    pygame.K_KP_DIVIDE: 0xa,
    pygame.K_KP_MULTIPLY: 0xb,
    pygame.K_KP_MINUS: 0xc,
    pygame.K_KP_PLUS: 0xd,
    pygame.K_KP_ENTER: 0xe,
    pygame.K_KP_PERIOD: 0xf,
}


class Screen(threading.Thread):
    def __init__(self):
        super().__init__()
        self.window_width = WIDTH * TILE_LEN
        self.window_height = HEIGHT * TILE_LEN
        self.width = WIDTH
        self.height = HEIGHT
        self.is_screen_on = False
        self.matrix = numpy.zeros((self.width, self.height), dtype=int)
        self.screen_lock = threading.Lock()
        self.keypad = {
            0: False,
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False,
            8: False,
            9: False,
            0xa: False,
            0xb: False,
            0xc: False,
            0xd: False,
            0xe: False,
            0xf: False,
        }

    def run(self):
        self.is_screen_on = True
        self.display = pygame.display.set_mode((self.window_width, self.window_height))

        while self.is_screen_on:
            self.handle_events()
            self.draw_screen()
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_screen_on = False
            if event.type == pygame.KEYDOWN:
                if event.key in KP_TRANSLATION_MAP:
                    self.keypad[KP_TRANSLATION_MAP[event.key]] = True
            if event.type == pygame.KEYUP:
                if event.key in KP_TRANSLATION_MAP:
                    self.keypad[KP_TRANSLATION_MAP[event.key]] = False

    def draw_screen(self):
        with self.screen_lock:
            for x in range(self.width):
                for y in range(self.height):
                    self.draw_tile(x, y, self.matrix[x, y])

    def draw_tile(self, x, y, value):
        rect = (x * TILE_LEN, y * TILE_LEN, (x + 1) * TILE_LEN, (y + 1) * TILE_LEN)
        if value == 1:
            pygame.draw.rect(self.display, (255, 255, 255), rect)
        elif value == 0:
            pygame.draw.rect(self.display, (0, 0, 0), rect)

    def draw_sprite(self, x, y, width, height, raw_sprite):
        """
        :param x: The sprite x coordinate.
        :param y: The sprite y coordinate.
        :param width: The sprite width.
        :param height: The sprite height.
        :param raw_sprite: The raw sprite in bytes.
        :return: If any screen pixel is flipped from set to unset.
        :return: 1 or 0 depending on if any pixel was flipped from set to unset.
        :rtype: int
        """
        with self.screen_lock:
            raw_sprite_value = int.from_bytes(raw_sprite, byteorder='big')
            sprite_matrix = self.bin_to_matrix(width, height, raw_sprite_value)
            set_to_unset = 0
            for col in range(width):
                for row in range(height):
                    matrix_x = (x + col) % self.width
                    matrix_y = (y + row) % self.height
                    if matrix_x < self.width and matrix_y < self.height:
                        last_value = self.matrix[matrix_x, matrix_y]
                        self.matrix[matrix_x, matrix_y] ^= sprite_matrix[col, row]
                        if last_value == 1 and self.matrix[matrix_x, matrix_y] == 0:
                            set_to_unset = 1

            return set_to_unset

    @staticmethod
    def bin_to_matrix(width, height, value):
        sprite_matrix = numpy.zeros((width, height), dtype=int)
        bit_index = (width * height) - 1
        bit_mask = 2 ** bit_index

        for y in range(height):
            for x in range(width):
                sprite_matrix[x, y] = (value & bit_mask) >> bit_index
                bit_index -= 1
                bit_mask = 2 ** bit_index

        return sprite_matrix

    def key_status(self, key):
        return self.keypad[key]

    def await_key(self):
        pressed_key = None
        while not pressed_key:
            for key in self.keypad:
                if self.keypad[key]:
                    pressed_key = key
        return pressed_key

    def clear_screen(self):
        with self.screen_lock:
            for x in range(self.width):
                for y in range(self.height):
                    self.matrix[x, y] = 0

