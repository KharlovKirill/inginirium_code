import random
import pygame

pygame.init()

W, H = 500, 500
GRAY=[75,] * 3
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("starry sky")
FPS = 10


class Star:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.color = (255,) * 3

    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), 5)

    def dark(self):
        if self.color[0] > 0:
            self.color = (self.color[0] - 1,) * 3

class Star_ship:

    def __init__(self):
        self.taels = []
        self.taels.append()
    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), 5)

    def dark(self):
        if self.color[0] > 0:
            self.color = (self.color[0] - 1,) * 3
x = 0
y = x

stars = []
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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

    if pygame.mouse.get_pressed()[0]:
        stars.append(Star())
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        win.fill((0,)*3)
    for star in (stars):
        star.draw(win)
        star.dark()
    for _ in range (10):
        pygame.display.update()
    pygame.time.delay(10)
    pygame.draw.circle(win, GRAY, (random.randint(0, W), random.randint(0, H)), 1)
    pygame.display.update()
    clock.tick(FPS)