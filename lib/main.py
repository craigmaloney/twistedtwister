#!/usr/bin/env python

'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "lib"
directory.
'''
import os, sys
import pygame, random
from pygame.locals import *
import tornado, house, player, ray, lightning, level, score, status, spark
from tornado import Tornado
from house import House
from player import Player
from ray import Ray
from lightning import Lightning
from spark import Spark
from level import Level
from score import Score
from status import Status
import data

SCREENRECT = Rect(0,0,800,600)

def start_game(level):
	enemy_list = level.get_enemies()
	max_fujita = enemy_list[0]
	for i in range(0,7):
		Tornado(enemy_list.pop(0))
	return max_fujita

def kill_objects(object):
	for i in object:
		i.kill()

class Title(pygame.sprite.Sprite):
        def __init__(self,text,color):
                pygame.sprite.Sprite.__init__(self,self.containers)
                self.font = pygame.font.Font(data.filepath(os.path.join('fonts','AT-BATACK.TTF')),90)
                self.image = pygame.Surface([200,26])
                self.rect = self.image.get_rect()
                self.text = text
                self.image = self.font.render(self.text,1,color)
                self.rect = self.image.get_rect()
                self.rect.center = (SCREENRECT.center)
        def update(self):
                (x,y) = SCREENRECT.center
                offx = random.randrange(-2,4)
                offy = random.randrange(-2,4)
                self.rect.center = (x+offx,y+offy)

def game(score_state):
	# No sound. :(
        #pygame.mixer.pre_init(44100,8,4,1024)
        pygame.init()
        pygame.font.init()
        #pygame.mixer.music.set_volume(2.0)
#        if pygame.mixer.music.get_busy():
#                pass
#        else:
#                musicfile = data.filepath('midi','bumblbee.mid')
#                pygame.mixer.music.load(musicfile)
#                pygame.mixer.music.play(-1)
	
	screen = pygame.display.set_mode(SCREENRECT.size)
	clock = pygame.time.Clock()
	background = pygame.image.load(data.filepath('images/new_background.png')).convert()
	level = Level()

	tornadoes = pygame.sprite.Group()
	houses = pygame.sprite.Group()
	player = pygame.sprite.Group()
	rays = pygame.sprite.Group()
	lightnings = pygame.sprite.Group()
	all = pygame.sprite.OrderedUpdates()
	titles = pygame.sprite.Group()
	statuses = pygame.sprite.Group()
	scores = pygame.sprite.Group()
	sparks = pygame.sprite.Group()
	
	start_new_game = False

	Score.containers = all
	Status.containers = all
	Title.containers = all
	Tornado.containers = tornadoes,all
	House.containers = houses,all
	Ray.containers = rays,all
	Lightning.containers = lightnings,all
	Score.containers = all
	Spark.containers = all
	Status.containers = all
	Player.containers = all

	screen.blit(background,(0,0))
        pygame.display.flip()

	# Title Screen
	score = Score(score_state)
	status_pause = 0
	first_time = True

        while start_new_game == False:
                status_pause = status_pause + 1
                if (first_time):
                        title_text = "Twisted Twister!"
                        Title(title_text,(0,0,0))
                        Title(title_text,(255,0,0))
                        Title(title_text,(0,255,255))
                        Title(title_text,(0,255,0))
                        Title(title_text,(0,0,255))
                        first_time = False
                for event in pygame.event.get():
                        if event.type == QUIT:
                                sys.exit()
                        if event.type == MOUSEBUTTONDOWN:
                                start_new_game = True
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        sys.exit()
                                else:
                                        start_new_game = True

                if status_pause > 100:
			Status ("Press any key to start...")
                        status_pause = 0
                all.clear(screen,background)
                all.update()
                dirty = all.draw(screen)
                pygame.display.update(dirty)
                clock.tick(30)
	kill_objects(all)

	house_container = []
	# Stuff to do to start the game
	#for i in range(100,800,150):
	for i in range(0,5):
		house_container.append(House(((i*150)+100,500)))

	# Reset the level
	level.start()

	# Start the scoreboard
	score = Score(score_state)

	# Populate the screen with the actors
	fujita = start_game(level)
	player = Player((400,550))

	# Lights! Camera! Silence on the set!
	playing = True
	bonus_house = 0
	last_bonus = 0
	bonus_at = 10000

	# Cameras rolling...
	# 3...2...1... Action!
	while playing:
		active = True
		lightning_counter = 0
		Status("Level %d, %s spotted!" % (level.get_level(), 'F' + str(fujita) + 's'))
		if (bonus_house > 0):
			for t in range(0,5):
				if (house_container[t].is_alive() == False):
					if (bonus_house >= 1):
						house_container[t].set_alive()
						bonus_house = bonus_house - 1
		while active:
			lightning_counter = lightning_counter + 1
			if lightning_counter > min(300,10000 - (level.get_level() * 200)):
				Lightning(player.get_position()) 
				lightning_counter = 0
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				if event.type == KEYDOWN:
					# Put in an escape key / Q key handler
					if event.key == K_ESCAPE:
						active = False
						playing = False
					if event.key == K_LEFT:
						player.left()
					if event.key == K_RIGHT:
						player.right()
					if event.key == K_LCTRL or event.key == K_RCTRL:
						player.fire()
				if event.type == KEYUP:
					if event.key == K_LEFT:
						player.stop()
					if event.key == K_RIGHT:
						player.stop()
					pass

			tornado_house_collide = pygame.sprite.groupcollide(houses,tornadoes,False,False)
			if (tornado_house_collide):
				for house in (tornado_house_collide):
					for tornado in (tornado_house_collide[house]):
						if (house.is_alive()):
							tornado.rise()
							house.rise(tornado.get_fujita())
			tornado_ray_collide = pygame.sprite.groupcollide(tornadoes,rays,False,False)
			if (tornado_ray_collide):
				for tornado in (tornado_ray_collide):
					tornado.hit(score)
			if (not tornadoes.sprites()):
				active = False
			lightning_player_collide = pygame.sprite.spritecollide(player,lightnings,False)
			if (lightning_player_collide):
				player.hit()
				Spark(player.get_midtop_position())

			if (score.get_score() >= (last_bonus + bonus_at)):
				bonus_house = bonus_house + 1
				# Should return the last score at 10,000 increments
				last_bonus = (score.get_score() / 1000) * 1000
				Status("Bonus!")
			all.clear(screen,background)
			all.update() 
			dirty = all.draw(screen) 
			pygame.display.update(dirty)
			clock.tick(30)

		# Reset for the next level
		if playing:
			level.next_level()	
			player.kill()
			fujita = start_game(level)
			player = Player((400,550))
			lightning_counter = 0
			houses_alive = False
			for i in range(0,5):
				house_container[i].restoration()
				houses_alive = houses_alive or house_container[i].is_alive()
			if (houses_alive or bonus_house > 0):
				playing = True
				active = True
			else:
				active = False
				playing = False
	score_state = score.get_score_state()
	kill_objects(all)
	return (score_state)
			

def main():
	high_score = 0
	score = 0
	while 1:
		score_state = (0,high_score)
		(score, high_score) = game(score_state)
	sys.exit()

if __name__ == '__main__':
	main()
