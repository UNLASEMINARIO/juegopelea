import pygame

class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
        
class boton(pygame.sprite.Sprite):
    def __init__(self,conluz,sinluz,x=200,y=200):
        self.imagen_normal=conluz
        self.imagen_seleccion=sinluz
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
        
    
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
def main():
    pygame.init()
    pantalla=pygame.display.set_mode((600,480))
    salir=False
    reloj1=pygame.time.Clock()
    menu=pygame.image.load("imagen/menu1.png")
    conluz=pygame.image.load("imagen/boton1.png")
    sinluz=pygame.image.load("imagen/boton2.png")
    conluz1=pygame.image.load("imagen/boton3.png")
    sinluz1=pygame.image.load("imagen/boton4.png")
    pygame.mixer.music.load("sonido/ARCADE2015.mp3")
    sonidoselect=pygame.mixer.Sound("sonido/sonidoselect.wav")
    botonini=boton(conluz,sinluz,320,50)
    botonsal=boton(conluz1,sinluz1,320,125)
    cursor1=cursor()
    pygame.mixer.music.play(2)
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botonini.rect):
                    sonidoselect.play()
                if cursor1.colliderect(botonsal.rect):
                    sonidoselect.play()
                    salir=True
            if event.type==pygame.QUIT:
                salir=True
        reloj1.tick(30)
        cursor1.update()
        pantalla.blit(menu,(0,0))
        botonini.update(pantalla,cursor1)
        botonsal.update(pantalla,cursor1)
        pygame.display.update()
    
    pygame.quit()

main()