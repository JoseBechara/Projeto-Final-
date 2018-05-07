# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:45:41 2018

@author: luiza
"""

import pygame
from random import randrange
import sys
from pygame.locals import *

pygame.init()
FPS = 10
preto=(0,0,0)
azul=(0,0,255)

largura=450
altura=600

tamanho=100


class Quadrado(pygame.sprite.Sprite):
  
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vel_y = vel_y
        
       
    
    def move(self):
        keys=pygame.key.get_pressed()
        if self.rect.y<altura-100:  
           if self.rect.x>=50:
              if keys[pygame.K_LEFT]:
                self.rect.x -= 50
           if self.rect.x <= largura-150: 
              if keys[pygame.K_RIGHT]:
                self.rect.x+=50
           if self.rect.y<altura-100:        
             if keys[pygame.K_DOWN]:
                self.rect.y+=20      
        
       
            
    def cair(self):
        self.rect.y += self.vel_y
        if self.rect.y >= altura-100:
            self.vel_y=0
        
    def do(self):
        self.move()
        self.cair()


fundo=pygame.display.set_mode((largura,altura))
pygame.display.set_caption("tetrinet")

quadrado = Quadrado('quadradoazul.jpeg', 200, 0, 10)
pecas_grupo = pygame.sprite.Group()
pecas_grupo.add(quadrado)

clock = pygame.time.Clock()

sair=True

while sair:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    
    
    fundo.fill(preto)   
     
    quadrado.do() 
    
    pecas_grupo.draw(fundo)
    
    pygame.display.update()

    
            
            
         
        #print(event)         
                
  
pygame.quit()        