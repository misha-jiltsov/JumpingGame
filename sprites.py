import pygame.sprite
from os import listdir
from os.path import isfile, join

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ACCELERATION = 9.81


class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        self.cooldown = 0
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = 64, 64
        self.colour = "blue"
        self.image = pygame.image.load("sprite_files/player.png")
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.rect.x = posx
        self.rect.y = posy

        self.velocity = [0, 0]

    def check_self_position(self):
        if self.rect.x < 0 or self.rect.x > 500 or self.rect.y < 0 or self.rect.y > 500:
            self.kill()

    def getpos(self):
        return self.rect.x, self.rect.y

    def updateposition(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.velocity[1] = self.velocity[1] + ACCELERATION * (1 / 60)
        if self.cooldown > 0:
            self.cooldown -= 1

    def setvelocityx(self, x):
        self.velocity[0] = x

    def setvelocityy(self, y):
        self.velocity[1] = y

    def jump(self):
        if self.cooldown == 0:
            self.setvelocityy(-4)
            self.cooldown = 30


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, posx, posy, velx, vely):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = 32, 32
        self.images = [f for f in listdir(r"C:\Users\misha\PycharmProjects\GameOfLife\sprite_files\obstacle") if
                       isfile(join(r"C:\Users\misha\PycharmProjects\GameOfLife\sprite_files\obstacle", f))]
        self.image = pygame.image.load(join(r"sprite_files\obstacle", self.images[0])).convert()
        self.curimage = 0
        self.numframes = len(self.images)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.tick = 1
        self.velocity = [velx, vely]

    def updateframe(self):
        self.tick += 1
        if self.tick % 15 == 0:
            if self.curimage + 1 == self.numframes:
                self.curimage = 0
            else:
                self.curimage += 1
            self.image = pygame.image.load(join(r"sprite_files\obstacle", self.images[self.curimage])).convert()

