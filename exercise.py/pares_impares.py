# -*- coding: utf-8 -*-
__author__     = "Ronivaldo Domingues de Andrade"
__course__     = "Engenharia Elétrica - 2º Período"
__university__ = "Universidade Federal do Rio de Janeiro"
__version__    = "1.0"
__date__       = "27/04/2021"
__python__     = "3.7"
#
import os
from random import sample
#
def main()->None:
    '''Essa função irá criar uma pasta compondo os nomes fonecidos pelo usúario e dentro dela irá criar 3 arquivos
    dois com os nomes fornecidos na hora da criação e o terceiro com a composição dos nomes fornecidos, em seguida irá pedir ao
    usuario um numero inteiro e a partir dele irá separar em cada arquivo os pares dos impares e no terceiro unir os númeroas
    de forma ordenada'''
    try:
        print('\t\t A QUALQUER MOMENTO PRECIONE CTRL + C PARA SAIR DO JOGO\n')
        while True:
            try:
                pares = input('\t- Dê um nome ao aquivo que armazenará os números pares: ')
                impares = input('\t- Dê um nome ao aquivo que armazenará os números ímpares: ')
                if((not pares[0].isdigit()) and (not impares[0].isdigit()) and (pares != impares)):
                    break
                else:
                    print('\n\t------------------------------------------------------------------------')
                    print('\t* OBSERVAÇÃO:\n\t\t- Procure dar nomes que não comecem com algarismos, e\n\t\t- Nomes diferentes para cada conjunto de elemento;')
                    print('\t------------------------------------------------------------------------\n')
            except IndexError:
                print('\n\t------------------------------------------------------------------------')
                print('\t* OBSERVAÇÃO:\n\t\t- Não deixe nenhum conjunto sem nome.')
                print('\t------------------------------------------------------------------------\n')
        caminhos = './'+pares+impares+'/'
        caminho = ''
        for i in caminhos:
            if i != ' ':
                caminho += i
        try:
            os.mkdir(caminho)
        except Exception:
            print('\t\t* A pasta [{}]já existe'.format(caminho[2:]))
        while True:
            try:
                print('\n\t------------------------------------------------------------------------')
                n = int(input('\t- Digite um valor inteiro qualquer: '))
                break
            except (ValueError, TypeError):
                print('\n\t------------------------------------------------------------------------')
                print('\t* OBSERVAÇÃO:\n\t\t- Entre apenas com números inteiros.')
                print('\t------------------------------------------------------------------------\n')
        caminho_pares = caminho+pares+'.txt'
        caminho_impares = caminho+impares+'.txt'
        par = open(caminho_pares, 'w')
        impar = open(caminho_impares, 'w')
        numeros = sample(range(n+1), n+1)
        for i in numeros:
            if(i%2 == 0):
                par.write(str(i)+'\n')
            else:
                impar.write(str(i)+'\n')
        par.close()
        impar.close()
        caminho_final = caminho+pares+impares+'.txt'
        par = open(caminho_pares,'r')
        impar = open(caminho_impares, 'r')
        inteiros = par.read().split('\n')+impar.read().split('\n')
        inteiro = []
        for i in inteiros:
            if i != '':
                inteiro.append(int(i))
        inteiro.sort()
        final = open(caminho_final, 'w')
        for i in inteiro:
            final.write(str(i) + '\n')
        final.close()
        par.close()
        impar.close()
        while True:
            print('\n\t------------------------------------------------------------------------')
            X = input('\t+ Deseja escolher outros números?(ENTER-->SIM, n-->NÃO)')
            print('\t------------------------------------------------------------------------\n')
            if(X == ''):
                main()
            else:
                break
        print('\t** O nome e o local do arquivo criado é:[{}].'.format(caminho_final))
    except KeyboardInterrupt:
        print('você precionou CTRL + C, então Saiu!')
    except Exception as d:
        print('Você fez algo errado, com a mensagem seguinte:', d, ',por isso saiu do jogo')
    pass
#
if __name__ == '__main__':
    '''Comando para inicializar o jogo'''
    main()
    pass
