import pygame
import sys

from settings import *
from sprite_sheet import Spritesheet




class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption('The Adventures of Bryce')
        self.clock = pygame.time.Clock()

        my_spritesheet = Spritesheet('sprite_sheets/slime_sprite_sheet.png')
        self.slime = [my_spritesheet.parse_sprite('slime_idle_0.png'), my_spritesheet.parse_sprite('slime_idle_1.png')]

    def run(self):

        index = 0

        my_event = pygame.USEREVENT + 0
        pygame.time.set_timer(my_event, 300)

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == my_event:
                    index = (index + 1) % len(self.slime)

            self.screen.fill('Black')
            self.screen.blit(self.slime[index], (0, DISPLAY_HEIGHT - 32))
            #print(index)
            #print(f'clock tick = {self.clock.tick()}')
            #index = (index + 1) % len(self.slime)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()