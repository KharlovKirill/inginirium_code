import random

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

class Cr:
    def __init__(self, color, x, y, rad):
        self.col = color
        self.x = x
        self.y = y
        self.rad = rad
        self.dir = 'r'

    def horizontal_move(self):
        if self.x > 500 - self.rad:
            self.dir = 'l'
        elif self.x < 0 + self.rad:
            self.dir = 'r'
        if self.dir == 'r':
            self.x += 3
        elif self.dir == 'l':
            self.x -= 3
            
    def draw(self, root):
        pygame.draw.circle(root, self.col, (self.x, self.y), self.rad)

FPS = 80
F = 0
clock = pygame.time.Clock()
cir = []
for i in range(100):
    cir.append(Cr(random.choices(range(256), k=3), i * 10, i * 5, 30))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for i in range(100):
        cir[i].horizontal_move()
    win.fill((255,255,255))
    for i in range(100):
        cir[i].draw(win)
    pygame.display.update()
    clock.tick(FPS)
