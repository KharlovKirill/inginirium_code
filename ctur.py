import random
import pygame

pygame.init()

W, H = 500, 500
GRAY=[75,] * 3
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("starry sky")
FPS = 1


class Star:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.color = (255,) * 3

    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), 5)

    def dark(self):
        if self.color[0] > 0:
            self.color = (self.color[0] - 1,) * 3


stars = []
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if pygame.mouse.get_pressed()[0]:
        stars.append(Star())
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        win.fill((0,)*3)
    for star in (stars):
        star.draw(win)
        star.dark()
    for _ in range (10):
       pygame.draw.circle(win, GRAY, (random.randint(0, W), random.randint(0, H)), 1)
    pygame.display.update()
    clock.tick(FPS)