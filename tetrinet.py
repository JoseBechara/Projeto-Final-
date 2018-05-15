from random import randrange
import sys
import pygame
from pygame.locals import *

pygame.init()
FPS = 10
preto=(0,0,0)
azul=(0,0,255)

largura=500
altura=600





class Quadrado(pygame.sprite.Sprite):
  
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.image.load(arquivo_imagem).convert()
#        self.image = pygame.Surface((100,100))
#        self.image.fill(azul)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y        
       
    
    def move(self):
        keys=pygame.key.get_pressed()
        if self.rect.x>=50:
            if keys[pygame.K_LEFT]:
               self.rect.x -= 100
        if self.rect.x <= largura-150: 
            if keys[pygame.K_RIGHT]:
               self.rect.x += 100
#        if self.rect.y<600:
#            if keys[pygame.K_DOWN]:
#                self.rect.y +=30
            

        
        
class Chao(pygame.sprite.Sprite):
  
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((700,2))
        self.image.fill(preto)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
     
    

fundo=pygame.display.set_mode((largura,altura))
pygame.display.set_caption("tetrinet")


quadrado = Quadrado('Peca3.png', 200, 0)
pecas_grupo = pygame.sprite.Group()
pecas_paradas_grupo = pygame.sprite.Group()
pecas_grupo.add(quadrado)

chao = Chao(0,600)
chao_grupo = pygame.sprite.Group()
chao_grupo.add(chao)



clock = pygame.time.Clock()
jogo=True


vel_y = 20

while jogo:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
            
    colisao = pygame.sprite.spritecollide(quadrado, chao_grupo, False)
    for e in colisao:
        vel_y=0
        for i in pecas_grupo:
            pecas_paradas_grupo.add(i)
        quadrado.rect.y=altura-100    
        
        
         

   
    colisao = pygame.sprite.spritecollide(quadrado, pecas_paradas_grupo, False)
    for e in colisao:
        vel_y = 0
        for p in pecas_grupo:
            pecas_paradas_grupo.add(p)
            
            
        
    if vel_y == 0:
        aleatorio = randrange(1,7)
        if aleatorio == 1:
            quadrado = Quadrado('Peca3.png', 200, 0)
            pecas_grupo.add(quadrado)
        if aleatorio == 2:
            pass
        if aleatorio == 3:
            pass
        if aleatorio == 4:
            pass
        if aleatorio == 5:
            pass
        if aleatorio == 6:
            pass
        if aleatorio == 7:
            pass
        vel_y = 20
        
        
      
        
    

    quadrado.rect.y += vel_y
    

        
        
            
    
    
    fundo.fill(preto)
    quadrado.move() 
    pecas_grupo.draw(fundo)
    
    pygame.display.update()

    
    
         
                 
                
  
pygame.quit()