import pygame
pygame.init()

W , H = 500, 500
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("игра про 25.000.000 котов  в мазде")
FPS = 80
def random_color():
    import random
    return random .choices (range(256), k=3)
clock = pygame.time.Clock()
while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    x, y = pygame.mouse.get_pos()
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        win.fill((255,)*3)
    pygame.draw.circle(win, random_color() ,(x,y), 25)
    pygame.display.update()
    clock.tick(FPS)


