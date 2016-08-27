import pygame
class Card(pygame.sprite.Sprite):
    def __init__ (self, name, isCoreCard, description, firstAction, secondAction, x, y):
        super().__init__ ()
        self.image = pygame.image.load(r"images\attack.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.name=name
        self.isCoreCard =isCoreCard
        self.description=description
        self.firstAction=firstAction
        self.secondAction=secondAction
        self.cardPlayed = False


    def showCardBack(self):
        self.image = pygame.image.load(r"images\backcover.png")
