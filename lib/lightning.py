''' Lightning object '''
import os
import pygame
import data
import random
class Lightning(pygame.sprite.Sprite):
	def __init__(self,player):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.image.load(data.filepath(os.path.join('images/lightning.png')))
		x=(random.randrange(0,800))
		y=-20
		self.rect = self.image.get_rect(center = (x,y))
		self.dx = self.dy = 0
		(self.destx, self.desty) = player
		self.desty = 550
		self.speed = 15
		
	def update(self):
		self.rect.move_ip(self.dx, self.dy)
		x = self.rect.centerx
		y = self.rect.centery
		if (x>self.destx):
			self.dx= self.speed * -1
		if (x<self.destx):
			self.dx = self.speed
		self.dy = self.speed
		(top_x,top_y) = self.rect.midtop
		if (top_y > 600):
			self.kill()
