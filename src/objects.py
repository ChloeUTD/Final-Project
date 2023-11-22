import pygame

class Bush(pygame.sprite.Sprite):
    def __init__(self, img, pos=(1000,544)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.pos = pos
        
    def update(self):
        x, y = self.pos
        x -= 10
        self.pos = (x, y)

class Web(pygame.sprite.Sprite):
    def __init__(self, img, pos=(1000, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.pos = pos

    def update(self):
        x, y = self.pos
        x -= 10
        self.pos = (x, y)

class Lumberjack(pygame.sprite.Sprite):
    def __init__(self, img, pos=(1000, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.pos = pos

    def update(self):
        x, y = self.pos
        x -= 10
        self.pos = (x, y)