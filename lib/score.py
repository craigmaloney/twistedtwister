import pygame
import data

class Score(pygame.sprite.Sprite):
        def __init__(self,(score,highscore)):
                pygame.sprite.Sprite.__init__(self,self.containers)
                self.font = pygame.font.Font(data.filepath('fonts/betsy.ttf'),36)
                self.image = pygame.Surface([200,26])
                self.rect = self.image.get_rect()
                self.rect.topleft = (20,2)
                self.score = score
		self.highscore = highscore
        def update(self):
                text = "High Score: %06d     Score: %06d" % (self.highscore,self.score)
                self.image = self.font.render(text,1,(0,0,0))
                self.rect = self.image.get_rect()
                self.rect.topleft = (20,2)
        def add_score(self,additional):
                self.score = self.score + additional
		if self.score > self.highscore:
			self.highscore = self.score
        def get_score(self):
                return self.score
	def reset_score(self):
		self.score = 0

	def get_score_state(self):
		return (self.score,self.highscore)
