import random

import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20, 20))
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 150, 100
        self.dir = [random.random(), random.random()]

    def update(self):
        if self.rect.x + 20 >= 740 or self.rect.x <= 0:
            self.dir[0] *= -1

        if self.rect.y <= 0:
            self.dir[1] *= -1

        self.rect = self.rect.move(30 * self.dir[0], 30 * self.dir[1])

    def collisions(self):
        self.dir[1] *= -1
