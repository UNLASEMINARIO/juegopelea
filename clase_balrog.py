import pygame

balrog={}
sprite=[]
for i in range(1,4):
    a="recursos/imagen/balrog/balrog_00"+str(i)+".png"
    sprite.append(a)
balrog[0]=sprite
sprite=[]
for i in range(1,6):
    a="recursos/imagen/balrogpeleando/pelea1_00"+str(i)+".png"
    sprite.append(a)
balrog[1]=sprite
sprite=[]
for i in range(1,12):
    a="recursos/imagen/balrogpeleando2/pelea2_00"+str(i)+".png"
    sprite.append(a)
balrog[2]=sprite
sprite=[]
for i in range(3,8):
    a="recursos/imagen/balrogcorre/corre_00"+str(i)+".png"
    sprite.append(a)
balrog[3]=sprite
sprite=[]
for i in range(11,16):
    a="recursos/imagen/balrogcorre/corre_00"+str(i)+".png"
    sprite.append(a)
balrog[4]=sprite
sprite=[]
class balrog_class(pygame.sprite.Sprite):
    def __init__(self,jugador):
        pygame.sprite.Sprite.__init__(self)
        self.jugador=jugador
        self.max_speed=10
        self.salto=False
        self.defensa=False
        self.estado=0
        self.x=0
        self.y=110#ver esto???
        if self.jugador==2:
            self.x=300
        
        self.quieto=balrog[0]
        self.golpes=balrog[1]
        self.patadas=balrog[2]
        self.corre=balrog[3]
        self.corre1=balrog[4]
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
                
            if direccion == 'corre1':
                self.clip(self.corre1,self.estado)
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
                if key [pygame.K_s]:
                    self.update('patadas')
                if key[pygame.K_LEFT]:
                    self.update('corre')
                    self.update_posicion(-10,0)
                if key[pygame.K_RIGHT]:
                    self.update('corre1')
                    self.update_posicion(10,0)
                
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.update('quieto')
                if event.key==pygame.K_LEFT:
                    self.update('quieto1')
                    
            if event.type==pygame.KEYDOWN and self.jugador==2:
                if key [pygame.K_f]:
                    self.update('golpes')
                if key [pygame.K_g]:
                    self.update('patadas')
                if key[pygame.K_j]:
                    self.update('corre')
                    self.update_posicion(-10,0)
                if key[pygame.K_l]:
                    self.update('corre1')
                    self.update_posicion(10,0)
                
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_j:
                    self.update('quieto')
                if event.key==pygame.K_l:
                    self.update('quieto')