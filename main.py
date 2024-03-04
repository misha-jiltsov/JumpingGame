
import pygame
from pygame import K_LEFT, K_RIGHT, K_SPACE, K_a, K_d

from sprites import Player, Obstacle
import random

name = input("Enter your name")
gameactive = False
BACKGROUND_BLUE = (20, 89, 199)

pygame.init()
pygame.font.init()
gamefont = pygame.font.SysFont("Comic Sans MS", 30)
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode([screen_width, screen_height])

player_list = pygame.sprite.Group()
obstacle_list = pygame.sprite.Group()

player = Player(200, 200)
player_list.add(player)



def join(a, b):
    return str(a)+str(b)

done = False
timerunning = 0
clock = pygame.time.Clock()

def scatter():
    while len(obstacle_list)!=9:

        randomvel1 = random.choice([(random.randint(50, 150)/100+0.03), (random.randint(-150, -50)/100-0.03)])
        randomvel2 = random.choice([(random.randint(50, 150) / 100 + 0.03), (random.randint(-150, -50) / 100 - 0.03)])

        randomposx = random.choice([random.randint(300, 400), random.randint(20, 100)])
        randomposy = random.choice([random.randint(300, 400), random.randint(20, 100)])

        newObject = Obstacle(randomposx, randomposy, randomvel1, randomvel2)
        obstacle_list.add(newObject)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if not gameactive:
        if keys[K_SPACE]:
            gameactive = True

    if gameactive:
        if len(obstacle_list) == 0:
            scatter()

        collisionlist = pygame.sprite.spritecollide(player, obstacle_list, False)



        screen.fill(BACKGROUND_BLUE)
        player_list.draw(screen)
        obstacle_list.draw(screen)

        keys = pygame.key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            player.setvelocityx(-2)
        elif keys[K_d] or keys[K_RIGHT]:
            player.setvelocityx(2)
        else:
            player.setvelocityx(0)
        if keys[K_SPACE]:
            player.jump()


        for playerobject in player_list:
            playerobject.updateposition()

        for obs in obstacle_list:
            obs.updateself()

        ########### do kill

        if len(collisionlist)>0:
            for playerobject in player_list:
                player_list.remove(playerobject)
                done = True

        if player.getpos()[0]>500 or player.getpos()[0]<0 or player.getpos()[1]>500 or player.getpos()[1]<0:
            for playerobject in player_list:
                player_list.remove(playerobject)
                done = True

        timerunning+=(1/60)

        timedisplay = f"{int(timerunning//60)}:{int(timerunning%60) if len(str(int(timerunning%60))) == 2 else join('0', int(timerunning%60))}"
        textsurface = gamefont.render(timedisplay, False, (0, 0, 0))
        screen.blit(textsurface, (400, 450))

    clock.tick(60)
    pygame.display.flip()


with open("all_scores.csv", "a") as file:
    file.write(f"{timedisplay},{name}")


pygame.quit()









