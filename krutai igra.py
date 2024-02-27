import pygame
speed = 1
pygame.init()
win = pygame.display.set_mode((900, 900))
x = 0
y = x
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if x >= 60 or x <= 10 or y >= 60 or y <= 10:
        speed = 25
        color = (255, 0, 0)
    else:
        speed = 10
        color = (255, 255, 0)

    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]:
        x -= speed
    elif k[pygame.K_RIGHT]:
        x += speed
    elif k[pygame.K_UP]:
        y -= speed
    elif k[pygame.K_DOWN]:
        y += speed
    else:
        if x>250:
            x-=speed
        elif x<250:
            x += speed
        if y>250:
            y-=speed
        elif y<250:
            y += speed

    win.fill((0, 0, 0))
    win.fill((0,0,0))
    pygame.draw.circle(win,color,(x, y), 50)
    pygame.display.update()
    pygame.time.delay(10)