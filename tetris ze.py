# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:37:26 2018

@author: luiza
"""
import pygame
from random import randrange

largura_display=10*50
altura_display=12*50

pygame.init()
tela = pygame.display.set_mode((largura_display,altura_display))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

perdeu = False



FPS = 10

preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
white=(255,255,255)

class Tabuleiro:
    def __init__(self):
        self.tab=[]
        for i in range(16):
            self.tab.append([0]*10)


class Peca(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, largura, altura, matriz):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura_display/2
        self.rect.y = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if self.rect.x >= 50:
                        self.rect.x -= 50
                if event.key == pygame.K_RIGHT:
                    if self.rect.x <= largura_display-150:
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
        self.rect.x = 220
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
        self.rect.x = 220
        self.rect.y = 0

class Peca3(Peca):

    def __init__(self):

        arquivo_imagem = "peca3.png"
        matriz=[[1,1],
                [1,1]]
        largura = 50
        altura = 50

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 220
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
        self.rect.x = 220
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
        self.rect.x = 220
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
        self.rect.x = 220
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
        self.rect.x = 220
        self.rect.y = 0
        self.largura= largura
        self.altura= altura
        self.matriz= matriz
                    

class Chao(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((700,50))
        self.image.fill(vermelho)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
     




pecas_grupo = pygame.sprite.Group()
pecas_paradas_grupo = pygame.sprite.Group()


aleatorio = 3 #randrange(0,7)
if aleatorio == 3:
    peca = Peca3()
#    elif blablalba:
        
pecas_grupo.add(peca)

chao = Chao(0,altura_display)
chao_grupo = pygame.sprite.Group()
chao_grupo.add(chao)
vel_y = 20

#fim_do_jogo = False

while not perdeu:
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            perdeu = True

    for i in pecas_grupo:
        i.rect.y += vel_y
#        if i.rect.y==0:
#          perdeu=True
   






    tela.fill(preto)
    pecas_grupo.draw(tela)
    chao_grupo.draw(tela)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()