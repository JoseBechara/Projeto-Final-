# -*- coding: utf-8 -*-

"""

Created on Tue Apr 24 15:27:59 2018



@author: Bruno Kaczelnik

"""

import json



lojas={}

with open('backup1.txt', 'r') as arquivo:

    lojas = json.loads(arquivo.read())



print('Controle de lojas')

print('0 - sair')

print('1 - adicionar loja')

print('2 - remover loja')

print('3 - entrar em uma loja')

print('4 - ver lojas')


escolha= input('Faça sua escolha:')



while escolha !='0':

    if escolha=='1' or escolha=='2' or escolha=='3':

        nome_loja = input('nome da loja:')

        if escolha == '1':

            if nome_loja in lojas:

                print ('esta loja ja existe')

            else:

                lojas[nome_loja]={}

                print ('loja ',nome_loja,'foi adicionada')

        elif escolha == '2':

            if nome_loja not in lojas:

                print('esta loja nao pode ser deletada... pois ela ja nao existe! ;)')

            else:

                del lojas[nome_loja]

                print ('{} foi deletada com sucesso'.format(nome_loja))            

        while escolha == '3':

            if nome_loja not in lojas:

                print('esta loja nao existe ,digite o nome correto da loja, ou "0" para sair.')

                nome_loja=input('em qual loja gostaria de entrar? ')
                
                if nome_loja == '0':
                    escolha = '0'
                else:
                    nome_loja=nome_loja

            else:

                print('Controle da loja ')

                print('0 - sair da loja ', nome_loja)

                print('1 - adicionar item')

                print('2 - remover item')

                print('3 - editar produto')

                print('4 - ver estoque')

                dloja=int(input('o que deseja fazer? '))

                if dloja == 0 :

                    escolha = '0'

                elif dloja== 1 or dloja== 2 or dloja== 3:

                    item = input ('qual o nome do produto? ')

                    if dloja == 1:

                        if item in lojas[nome_loja]:

                            print ('ja existe um item com este nome na loja ',nome_loja)

                        else:

                            lojas[nome_loja][item]={}

                            preco= float(input('qual o preco do produto?  '))

                            if preco < 0:

                                print ('o preco deve ser positivo')

                            else:

                                lojas[nome_loja][item]['preco']=preco

                                quantidade=int(input('qual a quantidade do novo produto?  '))

                                if quantidade<0:

                                    print('a quantidade deve ser positiva')

                                else:
                                

                                    lojas[nome_loja][item]['quantidade']=quantidade

                    elif dloja == 2:

                        if item not in lojas:

                            print ('este item nao existe no estoque')

                        else:

                            del lojas[nome_loja][item]

                    elif dloja==3:
                        
                        if item in lojas[nome_loja]:
                        
                            novo_preco=float( input('qual vais ser o novo preco do produto? '))
    
                            lojas[nome_loja][item]['preco']=novo_preco
 
                            nova_quantidade=int(input ('qual a quantidade que deseja adicionar ou subtrair?'))
 
                            x=lojas[nome_loja][item]['quantidade']

                            y=x+nova_quantidade

                            lojas[nome_loja][item]['quantidade']=y
                        
                        else:
                            print ("este produto nao existe")

                elif dloja==4:

                    faltando={}

                    m_total=0

                    for w in lojas[nome_loja]:

                        print ('{0}: quantidade={1}  preco=R${2}'.format(w,lojas[nome_loja][w]['quantidade'],lojas[nome_loja][w]['preco']))

                        if lojas[nome_loja][w]['quantidade'] < 0:

                            faltando[w]= lojas[nome_loja][w]['quantidade']

                        else:

                            x=w

                    for w in  faltando:

                        print('!!!!a quantidade de {0} no estoque e {1}!!!!'.format(w,faltando[w]))

                    for e in lojas[nome_loja]:

                        unitario=lojas[nome_loja][e]['preco']*lojas[nome_loja][e]['quantidade']

                        m_total += unitario

                    print('o valor monetario total do estoque e: ',m_total)

            

               

                else:

                    print ('este comando nao e valido')

    elif escolha == '4':

        for e in lojas:

            print(e)

    else:

        print('comando invalido')

    print('Controle de lojas')

    print('0 - sair')

    print('1 - adicionar loja')

    print('2 - remover loja')

    print('3 - entrar em uma loja')

    print('4 - ver lojas')

    

    escolha= input('o que mais voce deseja fazer:') 

    

    



print ('ate mais!!!')  



with open('backup1.txt', 'w') as arquivo:

    data = json.dumps(lojas, sort_keys=True, indent=4)

    arquivo.write(data)