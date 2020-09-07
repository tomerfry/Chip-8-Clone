"""
Module implement a class to generate instruction instances.
"""
import abc


class Instruction(object):

    def __init__(self, raw):
        self.raw = raw

    @abc.abstractmethod
    def affect_chip_state(self, registers, mem, stack, screen):
        raise NotImplementedError()


