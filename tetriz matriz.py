
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



FPS = 60

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
        self.rect.y = -50
        self.vel_y = 25

    def move(self):
        key = pygame.key.get_pressed()
       
        if key[pygame.KEYDOWN]:
             self.rect.y -= 50
        if key[pygame.K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x -= 50
        if key[pygame.K_RIGHT]:
            if self.rect.x <= largura_display - 100:
                self.rect.x += 50
                
    def cair(self):
        self.rect.y += self.vel_y



class Peca1(Peca):

    def __init__(self):

        arquivo_imagem = "Peca1.png"
        matriz=[[1,1],
                [1,0],
                [1,0],
                [1,0]]
        largura = int(50/2)
        altura = int(200/2)

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50

class Peca2(Peca):

    def __init__(self):

        arquivo_imagem = "Peca2.png"
        matriz=[[0,1,1],
                [1,1,0]]


        largura = int(150/2)
        altura = int(100/2)

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50

class Peca3(Peca):

    def __init__(self):

        arquivo_imagem = "Peca3.png"
        matriz=[[1,1],
                [1,1]]
        largura = int(100/2)
        altura = int(100/2)

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50
        


class Peca4(Peca):

    def __init__(self):

        arquivo_imagem = "Peca4.png"
        matriz=[[0,1,0],
                [1,1,1]]
        largura = int(150/2)
        altura = int(100/2)

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50


class Peca5(Peca):

    def __init__(self):

        arquivo_imagem = "Peca5.png"
        matriz=[[0,1],
                [1,1],
                [1,0]]
        largura = int(100/2)
        altura = int(150/2)

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50

class Peca6(Peca):

    def __init__(self):

        arquivo_imagem = "Peca6.png"
        matriz=[[0,1,0],
                [0,1,0],
                [0,1,0],
                [0,1,0]]
        largura = int(50/2)
        altura = int(200/2)

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50

class Peca7(Peca):

    def __init__(self):

        arquivo_imagem = "Peca7.png"
        matriz=[[0,0,0,1],
                [1,1,1,1]]
        largura = int(200/2)
        altura = int(100/2)

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50
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


delay = 0

peca_caindo = True
tab=[]
for i in range(24):
    tab.append([0]*20)

peca_caindo = True
lista_vel = []

while not perdeu:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            perdeu = True

    for i in pecas_grupo:
        x= int((i.rect.y)/50)
        y= int((i.rect.x)/50)
        
        if aleatorio == 3:
            if i.vel_y==0:
                tab[x][y] = 1
                tab[x+1][y] = 1
                tab[x][y+1] = 1
                tab[x+1][y+1] = 1

            if i.rect.y + 50  > altura_display - height or tab[x+2][y] == 1 or tab[x+2][y+1]:
                i.vel_y = 0
        lista_vel.append(i.vel_y)
        print(x)
        print(tab)
        
        if any([x == 50 for x in lista_vel]):
            lista_vel = []
            peca_caindo = True
        if any([x != 50 for x in lista_vel]):
            peca_caindo = False

        if i.rect.y == 0 and i.vel_y == 0:
            print('perdeu')
        

    if not peca_caindo:
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

    delay += 1
    if delay == 10:
        delay = 0
        peca.cair()


    peca.move()
    tela.fill(preto)
    pecas_grupo.draw(tela)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()
