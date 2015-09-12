import pygame

def terry():
    pygame.init()
    pantalla=pygame.display.set_mode((600,460),0,32)
    imagen=pygame.image.load("imagen/terry.png").convert_alpha()
    imagen1=pygame.image.load("imagen/fondo2.png")
    pygame.mixer.music.load("imagen/ARCADE2015.mp3")
    pos=(310,200)
    color=(255,255,60)
    salir=False
    terry={}
    terry[0]=(0,0,205,300)
    terry[1]=(203,0,207,300)
    terry[2]=(408,0,207,300)
    terry[3]=(615,0,207,300)
    terry[4]=(823,0,207,300)
    terry[5]=(1030,0,207,300)
    terry[6]=(1235,0,207,300)
    terry[7]=(1440,0,207,300)
    terry[8]=(1645,0,207,300)
    terry[9]=(1850,0,207,300)
    terry[10]=(2055,0,207,300)
    terry[11]=(2260,0,207,300)
    terry[12]=(0,0,205,300)
    cual=0
    ciclo=0
    reloj1=pygame.time.Clock()
    pygame.mixer.music.play(1)
    while salir!=True:
        ciclo=ciclo+1
        if ciclo>6:
            ciclo=0
            cual=cual+1
        if cual > 12:
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
terry()