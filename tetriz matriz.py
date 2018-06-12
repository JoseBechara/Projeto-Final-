
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:37:26 2018
@author: luiza
"""
import pygame
from random import randint
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
#from numpy import *

largura_display = 20*25
altura_display = 24*25

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
        self.click = False
        self.delay = 6
        self.caindo = True
        self.posicao = 1

    def move(self):
        key = pygame.key.get_pressed()
        x = int((self.rect.y)/25)
        y = int((self.rect.x)/25)

        if key[pygame.K_DOWN] and not self.click:
             self.delay = 6
             self.click = True
        if key[pygame.K_LEFT] and not self.click:
            self.click = True
            if not tab[x][y-1] == 1 and not tab[x+1][y-1] == 1:
                if self.rect.x >= 25:
                    self.rect.x -= 25
        if key[pygame.K_RIGHT] and not self.click:
            self.click = True
            if not tab[x][y+2] == 1 and not tab[x+1][y+2] == 1:
                if self.rect.x <= largura_display - 75:
                    self.rect.x += 25
        if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
            self.click = False

    def cair(self):
        self.rect.y += self.vel_y



class Peca1(Peca):

    def __init__(self):

        arquivo_imagem = "Peca1.png"
        matriz=[[1,1],
                [1,0],
                [1,0],
                [1,0]]
        largura = 25
        altura = 100

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


        largura = 75
        altura = 50

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
        largura = 50
        altura = 50

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
        largura = 75
        altura = 50

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
        largura = 50
        altura = 75

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
        largura = 25
        altura = 100

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
        largura = 100
        altura = 50

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        imagem = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(largura,altura))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = -50


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
var = 0
peca_caindo = True
tab = []
for i in range(24):
    tab.append([0]*20+[1])

k = 0
peca_caindo = True
lista_vel = []

while not perdeu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            perdeu = True

    #for i in pecas_grupo:
    x = int((peca.rect.y)/25)
    y = int((peca.rect.x)/25)

    if aleatorio == 3:
        if peca.rect.y-25  > altura_display - height or tab[x+2][y] == 1 or tab[x+2][y+1] == 1:
            # peca.vel_y = 0
            peca.caindo = False
            tab[x][y] = 1
            tab[x+1][y] = 1
            tab[x][y+1] = 1
            tab[x+1][y+1] = 1

        #print(x)
        #print(tab)
    if not peca.caindo:
        for z in range (24):
            for u in range(20):
                var += tab[z][u]
                if var == 20:
                    tab.remove(tab[z])
                    tab.insert(0,[0]*20+[1])
                    for peca in pecas_grupo:
                        if peca.rect.y == z*25:
                            pecas_grupo.remove(peca)
                        if peca.rect.y < z*25:
                            peca.rect.y += 25
                    var = 0
            var = 0

            k = 0

    if peca.rect.y == 0 and peca.vel_y == 0:
        print('perdeu')


    if not peca.caindo:
        peca.caindo = True
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
    if delay == peca.delay:
        delay = 0
        peca.cair()

    peca.move()
    tela.fill(preto)
    pecas_grupo.draw(tela)
    pygame.display.update()

    clock.tick(FPS)
print('oooooooooooooooooooooooooooooooooo')
print(tab)
pygame.quit()
quit()
