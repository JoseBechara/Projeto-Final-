
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:37:26 2018
@author: luiza
"""
import pygame
from random import randint
#from numpy import *

largura_display=10*50
altura_display=12*50

pygame.init()
tela = pygame.display.set_mode((largura_display,altura_display))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

perdeu = False



FPS = 5

preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
white=(255,255,255)

#class Tabuleiro:
#    def __init__(self):
#        self.tab=[]
#        for i in range(12):
#            self.tab.append([0]*10)
    


class Peca(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, largura, altura, matriz):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura_display/2
        self.rect.y = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 self.rect.y -= 25
            if event.type == pygame.K_LEFT:
                   self.rect.x -= 50
            if event.type == pygame.K_RIGHT:
                    if self.rect.x <= largura_display-100:
                        self.rect.x += 50
                        
   
        
        





class Peca1(Peca):

    def __init__(self):

        arquivo_imagem = "Peca1.png"
        matriz=[[1,1],
                [1,0],
                [1,0],
                [1,0]]
        largura = 50
        altura = 200

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0

class Peca2(Peca):

    def __init__(self):

        arquivo_imagem = "Peca2.png"
        matriz=[[0,1,1],
                [1,1,0]]


        largura = 150
        altura = 100

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0

class Peca3(Peca):

    def __init__(self):

        arquivo_imagem = "Peca3.png"
        matriz=[[1,1],
                [1,1]]
        largura = 100
        altura = 100

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0


class Peca4(Peca):

    def __init__(self):

        arquivo_imagem = "Peca4.png"
        matriz=[[0,1,0],
                [1,1,1]]
        largura = 150
        altura = 100

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0


class Peca5(Peca):

    def __init__(self):

        arquivo_imagem = "Peca5.png"
        matriz=[[0,1],
                [1,1],
                [1,0]]
        largura = 100
        altura = 150

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0

class Peca6(Peca):

    def __init__(self):

        arquivo_imagem = "Peca6.png"
        matriz=[[0,1,0],
                [0,1,0],
                [0,1,0],
                [0,1,0]]
        largura = 50
        altura = 200

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0

class Peca7(Peca):

    def __init__(self):

        arquivo_imagem = "Peca7.png"
        matriz=[[0,0,0,1],
                [1,1,1,1]]
        largura = 200
        altura = 100

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0
        self.largura= largura
        self.altura= altura
        self.matriz= matriz
                    

class Chao(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((600,50))
        self.image.fill(vermelho)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        self.tab=[]
        for i in range(1):
            self.tab.append([1]*10)




pecas_grupo = pygame.sprite.Group()
pecas_paradas_grupo = pygame.sprite.Group()


aleatorio = 3

if aleatorio  == 1:
    peca = Peca1()
    height  = 200
    
if aleatorio == 2:
    peca = Peca2()
    height = 100
    
if aleatorio == 3:
    peca = Peca3()
    height = 100
    
if aleatorio == 4:
    peca = Peca4()    
    height = 100
    
if aleatorio == 5:
    peca = Peca5()
    height = 150
    
if aleatorio == 6:
    peca = Peca6()
    height = 200
    
if aleatorio == 7:
    peca = Peca7()
    height = 100
    
pecas_grupo.add(peca)

def atualizar_tabuleiro(peca):
    pass
        

chao = Chao(0,altura_display)
chao_grupo = pygame.sprite.Group()
chao_grupo.add(chao)
vel_y =50

peca_caindo = True

#fim_do_jogo = False
cair= True
tab=[]
for i in range(12):
    tab.append([0]*10)
    
  
    
while not perdeu:
   
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            perdeu = True

    for i in pecas_grupo:
        i.rect.y += vel_y
        if i.rect.y + 50  > altura_display - height:
            vel_y = 0
        if vel_y == 0: 
            x= int((i.rect.y)/50)
            print(x)
            y= int((i.rect.x)/50)
            print(y)
            tab[x][y]= 1
            tab[x+1][y]=1
            tab[x][y+1]=1
            tab[x+1][y+1]=1
            print(tab)
            
    
#        for e in tab:
#            x= (i.rect.y)/50          
#            y= (i.rect.x)/50
#            if tab[x+2][y]==1:
#                vel_y= 0
#                if vel_y == 0: 
#                   x= (i.rect.y)/50          
#                   y= (i.rect.x)/50
#                   tab[x][y]= 1
#                   tab[x+1][y]=1
#                   tab[x][y+1]=1
#                   tab[x+1][y+1]=1
#                
#                elif tab[x+2][y+1]==1:
#                   vel_y=0
#                   if vel_y == 0: 
#                      x= (i.rect.y)/50          
#                      y= (i.rect.x)/50
#                      tab[x][y]= 1
#                      tab[x+1][y]=1
#                      tab[x][y+1]=1
#                      tab[x+1][y+1]=1
#                      
#                      
                      
                
         
        
#            
            
            
               
            
        
        
            
            
              
             
#    
    if not peca_caindo:
        aleatorio = 3

        if aleatorio  == 1:
            peca = Peca1()
            height  = 200
            
        if aleatorio == 2:
            peca = Peca2()
            height = 100
            
        if aleatorio == 3:
            peca = Peca3()
            height = 100
            
        if aleatorio == 4:
            peca = Peca4()    
            height = 100
            
        if aleatorio == 5:
            peca = Peca5()
            height = 150
            
        if aleatorio == 6:
            peca = Peca6()
            height = 200
            
        if aleatorio == 7:
            peca = Peca7()
            height = 100
            
        pecas_grupo.add(peca)
        
        
        #if vel_y == 0:
            
#        if i.rect.y==0:
#          perdeu=True
   






    tela.fill(preto)
    pecas_grupo.draw(tela)
    chao_grupo.draw(tela)
    pygame.display.update()

    clock.tick(FPS)
   
pygame.quit()
quit()