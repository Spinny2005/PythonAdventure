import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        try:
            self.image = pygame.image.load('./graphics/test/rock.png').convert_alpha()
        except FileNotFoundError:
            try:
                self.image = pygame.image.load('/home/spencer/PythonAdventure/graphics/test/rock.png').convert_alpha()
            except FileNotFoundError:
                self.image = pygame.image.load('$HOME/PythonAdventure/graphics/test/rock.png').convert_alpha()

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
