import pygame
pygame.init()

W , H = 500, 500
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("игра про 25.000.000 котов  в мазде")
FPS = 80

def load_img(name):
    img = pygame.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img
img =load_img('ing.png')
img1 = pygame.transform.scale(img, (200, 200))
img2 = pygame.transform.scale(img, (700, 700))

clock = pygame.time.Clock()
while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(FPS)

    win.fill('#FFED00')
    win.blit(img1,(0, 0))
    win.blit(img2, (100, 200))
    pygame.display.update()