import pygame
from random import randrange

largura_display=10*50
altura_display=16*50

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
        self.rect.x = 220
        self.rect.y = 0

    def move(self):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if self.rect.x>=50:
                    self.rect.x = -50
            if event.key == pygame.K_RIGHT:
                if self.rect.x <= largura_display-150:
                    self.rect.x = +50





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

    def __init__(self, pos_x, pos_y):

        arquivo_imagem = "Peca2.png"
        matriz=[[0,1,1]
                [1,1,0]]


        largura = 150
        altura = 100

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 0

class Peca3(Peca):

    def __init__(self, pos_x, pos_y):

        arquivo_imagem = "Peca3.png"
        matriz=[[1,1]
                [1,1]]
        largura = 50
        altura = 50

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 0


class Peca4(Peca):

    def __init__(self, pos_x, pos_y):

        arquivo_imagem = "Peca4.png"
        matriz=[[0,1,0]
                [1,1,1]]
        largura = 150
        altura = 100

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 0


class Peca5(Peca):

    def __init__(self, pos_x, pos_y):

        arquivo_imagem = "Peca5.png"
        matriz=[[0,1]
                [1,1]
                [1,0]]
        largura = 100
        altura = 150

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 0

class Peca6(Peca):

    def __init__(self, pos_x, pos_y):

        arquivo_imagem = "Peca6.png"
        matriz=[[0,1,0]
                [0,1,0]
                [0,1,0]
                [0,1,0]]
        largura = 50
        altura = 200

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 0

class Peca7(Peca):

    def __init__(self, pos_x, pos_y):

        arquivo_imagem = "Peca7.png"
        matriz=[[0,0,0,1]
                [1,1,1,1]]
        largura = 200
        altura = 100

        Peca.__init__(self, arquivo_imagem, largura, altura, matriz)

        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 0

class Chao(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((700,2))
        self.image.fill(preto)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        chao = Chao(0,600)
        chao_grupo = pygame.sprite.Group()
        chao_grupo.add(chao)
        chao = Chao(0,600)



lista_pecas = [Peca1, Peca2, Peca3, Peca4, Peca5, Peca6, Peca7]
pecas_grupo = pygame.sprite.Group()
pecas_paradas_grupo = pygame.sprite.Group()
for e in lista_pecas:
    Peca = e()
    pecas_grupo.add(e())

chao = Chao(0,600)
chao_grupo = pygame.sprite.Group()
chao_grupo.add(chao)
vel_y = 20

#fim_do_jogo = False

while not perdeu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            perdeu = True

    for i in pecas_grupo:
       if i.rect.y==0 and vel_y==0:
         perdeu=True






    tela.fill(preto)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()
