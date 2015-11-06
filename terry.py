import pygame
terry={}
sprite=[]
for i in range(1,12):
    a="recursos/imagen/terry/terry_00"+str(i)+".png"
    sprite.append(a)
terry[0]=sprite
sprite=[]
for i in range(1,37):
    a="recursos/imagen/terrypeleando/pelea1_00"+str(i)+".png"
    sprite.append(a)
terry[1]=sprite
sprite=[]
for i in range(1,29):
    a="recursos/imagen/terrypeleando2/pelea2_00"+str(i)+".png"
    sprite.append(a)
terry[2]=sprite
sprite=[]
for i in range(1,6):
    a="recursos/imagen/terrycorre/corre_00"+str(i)+".png"
    sprite.append(a)
terry[3]=sprite
sprite=[]
class terry_class(pygame.sprite.Sprite):
    def __init__(self,jugador):
        pygame.sprite.Sprite.__init__(self)
        self.jugador=jugador
        self.max_speed=10
        self.salto=False
        self.defensa=False
        self.estado=0
        self.x=0
        self.y=50#ver esto???
        if self.jugador==2:
            self.x=300
        
        self.quieto=terry[0]
        self.golpes=terry[1]
        self.patadas=terry[2]
        self.corre=terry[3]
        self.image=""
        self.clip(self.quieto,self.estado)
        
    def update_posicion(self,x,y):
            self.x=self.x+x
            self.y=self.y+y
        
    def clip(self,lista,estado):
            sprite=lista
            a=len(sprite)
            if estado >=a:
                self.estado=0
            self.image=sprite[self.estado]
        
    def update(self,direccion):
            if direccion == 'corre':
                self.clip(self.corre,self.estado)
                self.estado+=1
            
            if direccion=='quieto':
                self.clip(self.quieto,self.estado)
                self.estado+=1
            
            if direccion=='golpes':
                self.clip(self.golpes,self.estado)
                self.estado+=1
            
            if direccion=='patadas':
                self.clip(self.patadas,self.estado)
                self.estado+=1
        
    def handle_event(self,event):
            pygame.event.set_blocked(pygame.MOUSEMOTION)
            while pygame.event.get(): pass
            key =pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                game_over=True
            
            if event.type==pygame.KEYDOWN and self.jugador==1:
                if key [pygame.K_a]:
                    self.update('golpes')
                if key [pygame.K_d]:
                    self.update('patadas')
                if key[pygame.K_LEFT]:
                    self.update('corre')
                    self.update_posicion(-10,0)
                if key[pygame.K_RIGHT]:
                    self.update('corre')
                    self.update_posicion(10,0)
                
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
                    self.update('quieto')