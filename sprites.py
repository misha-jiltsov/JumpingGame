import pygame.sprite

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
ACCELERATION = 9.81

class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        self.cooldown = 0
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = 64, 64
        self.colour = "blue"
        self.image = pygame.image.load("sprite_files/player.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = posx
        self.rect.y = posy

        self.velocity = [0, 0]

    def check_self_position(self):
        if self.rect.x<0 or self.rect.x>500 or self.rect.y<0 or self.rect.y>500:
            self.kill()


    def getpos(self):
        return (self.rect.x, self.rect.y)


    def updateposition(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.velocity[1] = self.velocity[1]+ACCELERATION*(1/60)
        if self.cooldown>0:
            self.cooldown-=1

    def setvelocityx(self, x):
        self.velocity[0] = x
    def setvelocityy(self, y):
        self.velocity[1] = y

    def jump(self):
        if self.cooldown == 0:
            self.setvelocityy(-4)
            self.cooldown = 30

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = 32, 32
        self.image = pygame.image.load("sprite_files/obstacle.gif").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy