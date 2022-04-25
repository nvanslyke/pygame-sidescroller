import pygame
import os
import time
import random

print("unknown game by Nathan Van Slyke")
print()
print()

width = 850
height = 600
characterheight = 70
characterwidth = 70
boatwidth = 138
boatheight = 80
boomwidth = 50
boomheight = 50

background = (50,50,50)
water = (24,62,250)
sky = (135, 206, 235)
xplayer = 300
yplayer = 300
vel_x = 10
vel_y = 20
framerate = 60
jump = False
xboat = 800
boatspeed = 7
player = pygame.image.load(os.path.join('duck.png'))
player = pygame.transform.scale(player, (characterwidth, characterheight))
obstacle = pygame.image.load(os.path.join('boat.png'))
obstacle = pygame.transform.scale(obstacle, (boatwidth, boatheight))
explosion = pygame.image.load(os.path.join('explosion.png'))
explosion = pygame.transform.scale(explosion, (boomwidth, boomheight))

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("game")


def drawGame():
    window.fill(background)
    pygame.draw.rect(window, water, pygame.Rect(30, 30, 60, 60))
    
    pygame.display.update()

def enemy(dt):
    global xboat
    global boatspeed
    window.blit(obstacle, (xboat, 280))
    xboat -= boatspeed * dt
    if xboat < -150:
        xboat = 800

def collision():
    window.blit(explosion, (0, 280))

def main(xplayer, yplayer, vel_x, vel_y, jump):
    
    
    last_time = time.time()
    running = True
 
    while running:
        dt = time.time() - last_time
        dt *= framerate
        last_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(background)
        pygame.draw.rect(window, water, pygame.Rect(0, 330, 850, 500))
        pygame.draw.rect(window, sky, pygame.Rect(0, 0, 850, 330))
        window.blit(player, (xplayer, yplayer))
        enemy(dt)
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT] and xplayer > 0:
            xplayer -= vel_x * dt
        if keyPressed[pygame.K_RIGHT] and xplayer < 770:
            xplayer += vel_x * dt
        if jump is False and keyPressed[pygame.K_SPACE]:
            jump = True
        if jump == True:
            yplayer -= vel_y *dt
            vel_y -= 1 * dt
            if vel_y < -20:
                jump = False
                vel_y = 20  

        pygame.display.update()

        


    pygame.quit()


if __name__ == "__main__":
    main(xplayer, yplayer, vel_x, vel_y, jump)