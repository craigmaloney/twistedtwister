import os
import pygame
import data
class Status(pygame.sprite.Sprite):
        def __init__(self,text):
                pygame.sprite.Sprite.__init__(self,self.containers)
                self.font = pygame.font.Font(data.filepath(os.path.join('fonts','AT-BATACK.TTF')),72)
                self.image = pygame.Surface([200,26])
                self.rect = self.image.get_rect()
                self.text = text
                self.image = self.font.render(self.text,1,(0,0,0))
                self.rect = self.image.get_rect()
                self.rect.topleft = (850,400)
        def update(self):
                self.rect.move_ip(-10,0)
                if self.rect.right < 0:
                        self.kill()

