
     ///////////
    [__      __]
   +(    ) +
     [ /_,  .]  $
    (>- ----< )
    \/__- __/

import pygame
w

, h = [int(t) for t in input().split()]
pygame.init()
win = pygame.display.set_mode((w, h))
# win.fill((255,255,255))МММ
# pygame.draw.circle(win,(0,200,255),(150,50), 10)
# pygame.display.update()
win.fill((0, 0, 0))(0, 0), (w, h), 5)
pygame.draw.line(win, (255, 255, 25
                       pygame.draw.line(win, (255, 255, 255), 5), (w, 0), (0, h), 5)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()