"""
This module implements the screen class.
"""
import pygame

from consts import *


class Screen(object):
    def __init__(self):
        self.screen_width = WIDTH * TILE_LEN
        self.screen_height = HEIGHT * TILE_LEN
        self.screen_is_on = False
        self.display = None

    def turn_screen_on(self):
        self.screen_is_on = True
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))

        while self.screen_is_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.turn_screen_off()

    def turn_screen_off(self):
        self.screen_is_on = False