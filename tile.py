import pygame

from settings import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, position, groups):

        super().__init__(groups)
        self.image = pygame.image.load()