
import pygame

def terrycorre():
    pygame.init()
    pantalla=pygame.display.set_mode((662,460),0,32)
    imagen=pygame.image.load("imagen/terrycorre.png").convert_alpha()
    imagen1=pygame.image.load("imagen/fondo2.png")
    pygame.mixer.music.load("imagen/ARCADE2015.mp3")
    pos=(200,225)
    color=(255,255,60)
    salir=False
    terry={}
    terry[0]=(0,0,275,300)
    terry[1]=(290,0,275,300)
    terry[2]=(566,0,240,300)
    terry[3]=(800,0,275,300)
    terry[4]=(1090,0,275,300)
    terry[5]=(1350,0,275,300)
    
    cual=0
    ciclo=0
    reloj1=pygame.time.Clock()
    pygame.mixer.music.play()
    while salir!=True:
        ciclo=ciclo+1
        if ciclo>6:
            ciclo=0
            cual=cual+1
        if cual > 5:
                cual = 0
                cual=cual+1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
        reloj1.tick(60)       
        pantalla.fill(color)
        pantalla.blit(imagen1,(0,0))
        pantalla.blit(imagen,pos,terry[cual])
        pygame.display.update()    
    pygame.quit()
terrycorre()