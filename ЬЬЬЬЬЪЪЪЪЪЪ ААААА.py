import pygame
pygame.init()
win = pygame.display.set_mode((900, 900))
class Cr:
    def __init__(self,color,x,y,rad):

        self.h = 30
        self.col = color
        self.x = x
        self.y = y
        self.rad = rad
        self.is_jump = False

    def  move_by_keys(self):
        if self.is_jump:
            if self.h >= -30:
                self.y -= self.h
                self.h -= 3
            else:
                self.is_jump = False
                self.h = 30
        k = pygame.key.get_pressed()
        if k[pygame.K_a]:
           self.x -= 3
        elif k[pygame.K_d]:
            self.x += 3
        elif k[pygame.K_w]:
            self.y -= 3
        elif k[pygame.K_s]:
            self.y += 3

        if k[pygame.K_SPACE]:
            self.is_jump = True

    def draw(self,root):
        pygame.draw.circle(root,self.col,(self.x, self.y), self.rad)

c = Cr((170,250,250), 255, 250, 25)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    c.move_by_keys()
    win.fill((0,0,0))
    c.draw(win)
    pygame.display.update()
    pygame.time.delay(10)










 #                                   !!!!
#                  ///////////      !!!!-+
#                 [ __      __]     (())
#               +(  *  /    * ) +    ()
#                 [   /_,  . ]  $    ()
#                  (<крыса>) )      / /
#                  /___--___/      / /
  #              _____((()))_____(())
   #     &&&&  (()) ((((()))))
    #    %%%   ()   ((((()))))
     #   //    ()   ((((()))))
      #  ()   / /   ((((()))))
       #  =--/_/