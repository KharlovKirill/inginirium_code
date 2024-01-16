import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
x = 0
y = x
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = x + 1
    if x > 500:
        x = 0
    y = y + 1
    if y > 500:
        y =
    win.fill((0, 0, 0))
    win.fill((0,0,0))
    pygame.draw.rect(win,(0,255,255),(x,250, 50, 50))
    pygame.display.update()



    win.fill((0, 0, 0))
    win.fill((0,0,0))
    pygame.draw.rect(win,(	(0,255,0)),(y,250, 50, 50))
    pygame.display.update()
