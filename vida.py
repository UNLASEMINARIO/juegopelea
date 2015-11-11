import pygame

ancho, alto = 1024, 600
blue=(0,0,255)
red=(255,0,0)
yellow=(255,255,0)
grey=(150,150,150)
black=(0,0,0)

class HP_Bar(object):
    
    def __init__(self, screen, NumJug):
        self.screen = screen
        self.numJug = NumJug
    
    def draw(self, vida):
        if(vida<=25):
            color=red
        else:
            if(vida<=50):
                color=yellow
            else:
                color=blue
            
        if(self.numJug == 1):
            pygame.draw.rect(self.screen,black,(27,28,407,34),0)
            pygame.draw.rect(self.screen,black,(227,58,207,16),0)
            pygame.draw.rect(self.screen,grey,(30,30,400,30),0)
            pygame.draw.rect(self.screen,color,(430,30,-vida*4,30),0)
        else:
            pygame.draw.rect(self.screen,black,(ancho - 432,28,405,34),0)
            pygame.draw.rect(self.screen,black,(ancho - 432,58,205,16),0)
            pygame.draw.rect(self.screen,grey,(ancho - 430,30,400,30),0)
            pygame.draw.rect(self.screen,color,(ancho - 430,30,vida*4,30),0)
