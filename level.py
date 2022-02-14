import pygame

from settings import *

class Level:

    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_objects = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):

        for row_index, row in enumerate(WORLD_MAP):

            for column_index, column in enumerate(row):

                x = column_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if column == 'x':
                    pass

