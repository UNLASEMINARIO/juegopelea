import pygame
import clase_balrog
from pygame.constants import FULLSCREEN

pygame.init()
pantalla=pygame.display.set_mode((1024,600),FULLSCREEN)
salir=False
reloj1=pygame.time.Clock()
jugador = clase_balrog.balrog_class(1)

game_over = False
while game_over == False:
    reloj1.tick_busy_loop(30) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    jugador.handle_event(event)
    background=pygame.image.load("recursos/imagen/fondo5d.jpg").convert()
    pantalla.blit(background,(0,0))
##    print(player.image)
    surf = pygame.image.load(jugador.image).convert_alpha()
    surf=pygame.transform.scale(surf,(700,700))
##    print(player.estado)
    pantalla.blit(surf,(jugador.x,jugador.y))
    print(reloj1.get_fps())
    pygame.display.flip()
pygame.quit()