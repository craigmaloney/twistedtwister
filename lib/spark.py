import pygame
from pygame import *
import random
class Spark(pygame.sprite.Sprite):
        def __init__(self,pos):
                pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.Surface((5,5),SRCALPHA)
		self.image.fill([255,255,0])
                self.rect = self.image.get_rect(center = pos)
                self.alpha = 200
		self.dy = -5
		self.dx = random.randrange(-4,4)
        def update(self):
		self.rect.move_ip(self.dx, self.dy)
                self.alpha = self.alpha - 10
                self.image.set_alpha(self.alpha)
                if (self.alpha < 0):
                        self.kill()
		self.dy = self.dy + 1
