
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:37:26 2018
@author: luiza
"""
import pygame
from random import randint

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
        self.rect.y = -50


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


        




vel_y =50



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
            cair = False
            
        x= int((i.rect.y)/50)
        print(x)
        y= int((i.rect.x)/50)
        print(y)
        tab[x][y]= 1
        tab[x+1][y]=1
        tab[x][y+1]=1
        tab[x+1][y+1]=1
        
        tab[x-1][y]=0
        tab[x-1][y+1]=0
        print(tab)
        
    
#        for e in tab:
#            x= (i.rect.y)/50          
#            y= (i.rect.x)/50
#            if tab[x+2][y]==1:
#                vel_y= 0
#                if vel_y == 0: 
#                   x= int((i.rect.y)/50 )         
#                   y= int((i.rect.x)/50)
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

                                            
                      
                
            
            
               
            
        
        
            
            
              
                 
    if not cair:
        peca_caindo = True
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
        
        







    tela.fill(preto)
    pecas_grupo.draw(tela)
    pygame.display.update()

    clock.tick(FPS)
   
pygame.quit()
quit()