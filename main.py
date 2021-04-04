import pygame as pg
import math
import time

size = 800
modulo = 300
speed = 0.001

print("You can use keys 1/2/3/4/5/6/7/8/9 to set n number"+"\n"+
      "And you can press SPACE to stop the time")

window = pg.display.set_mode((size, size))

def drawLines(n, t, r, surface):
    coords = []
    pg.draw.circle(window, (255, 255, 255), (size/2, size/2), r, 1)
    for i in range(n):
        coords.append((math.cos(math.pi*2/n*i-math.pi/2)*r+r, math.sin(math.pi*2/n*i-math.pi/2)*r+r))

    for i in range(n):
        pg.draw.line(surface, (255, 255, 255), coords[i], coords[int(i*t%n)], 1)

launched = True
stop = False
i = 1
while launched:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            launched = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                stop = not stop
            if event.key == pg.K_1:
                i = 1
            if event.key == pg.K_2:
                i = 2
            if event.key == pg.K_3:
                i = 3
            if event.key == pg.K_4:
                i = 4
            if event.key == pg.K_5:
                i = 5
            if event.key == pg.K_6:
                i = 6
            if event.key == pg.K_7:
                i = 7
            if event.key == pg.K_8:
                i = 8
            if event.key == pg.K_9:
                i = 9
            
    window.fill((0, 0, 0))
    text = pg.font.Font(None, 24).render('n = '+"%.2f" % i, True, (255, 255, 255))
    window.blit(text, (20, 20))
    drawLines(modulo, i, size/2, window)
    if stop != True:
        i += speed
    pg.display.update()