
import pygame
from pygame import K_LEFT, K_RIGHT, K_SPACE, K_a, K_d

from sprites import Player, Obstacle
import random

BACKGROUND_BLUE = (20, 89, 199)

pygame.init()
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode([screen_width, screen_height])

player_list = pygame.sprite.Group()
obstacle_list = pygame.sprite.Group()

player = Player(200, 200)
player_list.add(player)


done = False

clock = pygame.time.Clock()

def scatter():
    for i in range(4):
        newObject = Obstacle(random.randint(1, 500), random.randint(1, 500))
        obstacle_list.add(newObject)


def deathanim():
    for obs in obstacle_list:
        obs.kill()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if len(obstacle_list) == 0:
        scatter()

    collisionlist = pygame.sprite.spritecollide(player, obstacle_list, False )



    screen.fill(BACKGROUND_BLUE)
    player_list.draw(screen)
    obstacle_list.draw(screen)

    keys = pygame.key.get_pressed()

    ###HORIZONTAL POS

    if keys[K_a] or keys[K_LEFT]:
        player.setvelocityx(-2)
    elif keys[K_d] or keys[K_RIGHT]:
        player.setvelocityx(2)
    else:
        player.setvelocityx(0)

    ######## JUMP

    if keys[K_SPACE]:
        player.jump()

    for playerobject in player_list:
        playerobject.updateposition()
        print(playerobject.getpos())

    if len(player_list) == 0:
        deathanim()
        done = True



    clock.tick(60)
    pygame.display.flip()






pygame.quit()









