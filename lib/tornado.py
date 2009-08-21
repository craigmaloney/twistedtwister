''' Tornado object:
'''
import pygame
import os
import data
import random
class Tornado(pygame.sprite.Sprite):
	def __init__(self,fujita):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.image.load(data.filepath(os.path.join('images','tornado.png')))
		self.fujita = fujita
		x=(random.randrange(0,2)*800)
		y=-200
		self.rect = self.image.get_rect(center = (x,y))
		self.rescale()
		self.dx = self.dy = 0
		self.destx = 0
		self.new_x()
		self.desty = 500
		self.frameskip = 4
		self.frames = 0
		self.speed = 1
                self.last_change = 0
		self.timer = 0
		self.initial_pause = random.randrange(100,300)
		
	def update(self):
		if self.initial_pause >0:
			self.initial_pause = self.initial_pause - 1
			return
		if self.timer > 0:
			self.timer = self.timer - 1
		if self.fujita < 0:
			self.die()
		else:
			self.rect.move_ip(self.dx, self.dy)
			self.frames = self.frames + 1
			if (self.frames > self.frameskip):
				self.frames = 0
				x = self.rect.centerx
				y = self.rect.centery
				self.last_change = self.last_change + 1
				if (x>self.destx):
					self.dx= (self.dx - self.speed)
				if (x<self.destx):
					self.dx = (self.dx + self.speed)
				if (y>self.desty):
					self.dy= (self.dy - self.speed)
				if (y<self.desty):
					self.dy = (self.dy + self.speed)
				if (y<-40 ):
					self.dy = 1
				if (y>500 ):
					self.dy = -1
				if (x<0):
					self.dx = 1
				if (x>800):
					self.dx = -1
			if (self.last_change > 75):
				self.new_x()

	
	def rise(self):
		self.dy = self.dy - self.speed

	def get_fujita(self):
		return self.fujita
	
	def hit(self,score):
		if (self.timer <= 0):
			self.fujita = self.fujita - 1
			self.dy = -2
			self.rescale()
			self.timer = 20
			score.add_score(100)

	def new_x(self):
		self.destx = random.randrange(200,600)
		self.last_change = 0
	
        def rescale(self):
		pos = self.rect.center
                scale_x = 200 - (100-(self.fujita*20))
                scale_y = 250 - (100-(self.fujita*20))
                self.image = pygame.transform.scale(self.image,(scale_x, scale_y))
                self.rect = self.image.get_rect(center = pos)

	def die(self):
		scale = (self.timer*5)
		pos = self.rect.center
		if self.timer > 0:
			self.image = pygame.transform.scale(self.image,(scale, scale))
			self.rect = self.image.get_rect(center = pos)
		else:
			self.kill()
