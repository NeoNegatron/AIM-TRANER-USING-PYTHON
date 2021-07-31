import math
import random
import pygame


pygame.init()

w = 800
h = 600
screen = pygame.display.set_mode((w,h))


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
cyan = (0,255,255)
fuschia = (255,0,255)
gold = (255,0,255)
lawn_green = (124,252,0)


colors = [black,white,red,yellow,cyan,fuschia,gold,lawn_green]



cx = random.randint(20,w-20)
cy = random.randint(20,h-20)
r = random.randint(10,20)
pygame.draw.circle(screen,random.choice(colors),(cx,cy),r)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()

    sqx = (x - cx)**2
    sqy = (y - cy)**2

    if math.sqrt(sqx + sqy) < r and click[0] == 1:
        screen.fill(black)  # Reset the screen
        cx = random.randint(20,w-20)
        cy = random.randint(20,h-20)
        r = random.randint(10, 20)
        pygame.draw.circle(screen, random.choice(colors), (cx, cy), r)

    pygame.display.update()
   