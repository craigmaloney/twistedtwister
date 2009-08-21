''' Tornado object
'''
import pygame
import os
import data
class House(pygame.sprite.Sprite):
	def __init__(self,pos):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.images = []
		for i in range(1,9):
			filename = os.path.join('images','house_000'+str(i)+'.png')
			self.images.append(pygame.image.load(data.filepath(filename)))

		self.framenumber = 7
		self.image = self.images[self.framenumber]
		self.rect = self.image.get_rect(center = pos)
		self.original_x = self.rect.centerx
		self.original_y = self.rect.centery
		self.max_damage = 10
		self.damage = self.max_damage
		self.dx = self.dy = 0
		self.timer = 0
		self.alive = True
	def update(self):
		if (not self.alive):
			return
		(x,y) = self.get_position()
		if (y < self.original_y):
			self.dy = self.dy + 1
		if (y > self.original_y):
			self.dy = 0
			self.rect.center = (x,self.original_y)
		self.rect.move_ip(self.dx, self.dy)
		if (y<=0):
			self.dy = 0
			self.alive = False
			self.rect.center = (self.original_x,-100)
		if self.timer > 0:
			self.timer = self.timer - 1
		self.image = self.images[self.framenumber]

	def rotate(self):
		if (not self.alive):
			return
		self.framenumber=self.framenumber+1
		if self.framenumber > 7:
			self.framenumber = 0
	def rise(self,fujita):
		if (not self.alive):
			return
		if self.damage < 0:
			self.dy = self.dy - 2
			self.rotate()
		else:
			if self.timer <= 0: 
				self.dy = self.dy - 1
				self.damage = self.damage - (fujita+1)
				self.timer = 10

	def get_position(self):
		return self.rect.center

	def restoration(self):
		if (not self.alive):
			return
		self.damage = self.damage + 5
		if self.damage > self.max_damage:
			self.damage = self.max_damage
	def bonus(self):
		if (not self.alive):
			return
		return(100)
	
	def is_alive(self):
		return (self.alive)

	def set_alive(self):
		self.alive = True
		self.damage = self.max_damage
		self.rect.center= (self.original_x,self.original_y)
		self.framenumber = 7
