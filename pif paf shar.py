import pygame

pygame.init()
from sprit.plait import Plain
from sprit.bal import Ball

W, H = 740, 800
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("игра про 25.000.000 котов  в мазде")
pygame.display.set_icon(pygame.image.load(r"C:\Users\a\Pictures\Screenshots\Снимок экрана 2024-03-19 191931.png"))

all_sprites = pygame.sprite.Group()
plain = Plain(690, all_sprites)
bal = Ball(all_sprites)
FPS = 90
F = 0
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if plain.rect.colliderect(bal.rect):
        bal.collisions()

    all_sprites.update()
    win.fill((0,) * 3)
    all_sprites.draw(win)
    pygame.display.update()
    clock.tick(FPS)