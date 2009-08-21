import pygame
from pygame.locals import *
import data

class Ray(pygame.sprite.Sprite):
	def __init__(self,pos):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.Surface((30,550),SRCALPHA)
		self.image.fill([255,255,0])
		self.rect = self.image.get_rect()
		self.rect.midbottom = pos
		self.timer = 5
	def update(self):
		self.timer = self.timer - 1
		self.alpha = self.timer * 50
		self.image.set_alpha(self.alpha)
		if self.timer < 0:
			self.kill()
