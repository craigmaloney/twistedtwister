'''Player classes'''

import pygame
import random
import os
import ray
from ray import Ray
import data

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		pygame.sprite.Sprite.__init__(self,self.containers)
		self.images = []
		for i in range(1,4):
			filename = os.path.join('images','player_000'+str(i)+'.png')
			self.images.append(pygame.image.load(data.filepath(filename)))
		self.framenumber = 1
		self.image = self.images[self.framenumber]
		self.rect = self.image.get_rect(center = pos)
		self.timer = 0
		self.firetimer = 0
		self.speed = 10
		self.dx = self.dy = 0
		self.damaged = False
	def update(self):
		self.rect.move_ip(self.dx, self.dy)
		(x,y) = self.rect.center
		x=min(max(x,15),800 - 15)
		self.rect.center = (x,y)
		if self.firetimer > 0:
			self.firetimer = self.firetimer - 1
		if (self.damaged and self.firetimer <= 0):
			self.damaged = False
	
	def left(self):
		if self.damaged:
			return()
		self.image = self.images[1] # Go forward
		self.dx = self.speed * -1

	def right(self):
		if self.damaged:
			return()
		self.image = self.images[0] # Go backward
		self.dx = self.speed

	def stop(self):
		self.dx = 0

	def get_position(self):
		return self.rect.center
	
	def get_midtop_position(self):
		return self.rect.midtop
	
	def fire(self):
		if self.firetimer <= 0:
			self.firetimer = 10
			Ray(self.get_midtop_position())

	def hit(self):
		self.firetimer = 50
		self.damaged = True
		self.image = self.images[2] # Ack! I've been hit!

