import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def _init_(self, game, x, y):

        self.game = game
        self.layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite._init_(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE