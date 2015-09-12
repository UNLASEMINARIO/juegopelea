import pygame

def main():
    pygame.init()
    pantalla=pygame.display.set_mode((600,480))
    salir=False
    reloj1=pygame.time.Clock()
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
        reloj1.tick(30)
        
        pygame.display.update()
    
    pygame.quit()

main()