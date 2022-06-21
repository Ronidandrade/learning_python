# -*- coding: utf-8 -*-

__author__     = "Ronivaldo Domingues de Andrade"
__course__     = "Engenharia Elétrica - 2º Período"
__university__ = "Universidade Federal do Rio de Janeiro"
__version__    = "1.0"
__date__       = "27/04/2021"
__python__     = "3.7"

from datetime import datetime
class EntraString(Exception):
    '''Classe que cria o erro para caracteres não numericos'''
    def __init__(self, msg):
        Exception.__init__(self, msg)
        pass
    pass
def lista_number()->None:
    '''Função que cria a lista de números a serem adivinhados pelo jogador'''
    lista_number = []
    while True:
        try:
            number = input('\t- Digite um número inteiro positivo:(E um NEGATIVO para encerrar)')
            if(number.isalpha()):
                raise EntraString('\t\t ATENÇÂO: Insira apenas números e Inteiros!')
            else:
                if(int(number) < 0):
                    break
                else:
                    lista_number.append(number)
        except EntraString as e:
            print('\t\t---------------------------------------------------')
            print(e)
            print('\t\t---------------------------------------------------')
        except Exception:
            print('\t\t---------------------------------------------------')
            print('\t\t ATENÇÂO: Insira apenas números e Inteiros!')
            print('\t\t---------------------------------------------------')
    return lista_number

def main()->None:
    '''Função que permite as jogadas pelo jogador e ao final registra em um arquivo seu desempenho e alguns dados'''
    print('------------------------------------------------------------------------------------')
    print('\t\t\t\t Jogo Acerte o Número')
    print('------------------------------------------------------------------------------------')
    l = list(set(lista_number()))
    X = l.copy()
    pontos = 0
    contador = 0
    acertos = []
    erros = []
    while(contador < 10 and len(X) > 0):
        print('------------------------------------------------------------------------------------')
        if((len(erros) + len(acertos)) != 0):
            print('\t- Tentativas já usadas: {}'.format(acertos + erros))
        n = input('\t- Você tem mesmo sorte? Qual é o número escondido? Acerte, se puder... ')
        if n in X:
            acertos.append(n)
            X.remove(n)
            pontos += 1
            print('\t\t---------------------------------------------------')
            print('\t\t !PARABÉNS! Você acertou!')
            if(len(X) > 0):
                print('\n\t\t    Faltam {} números para ser um vencedor. Vamos!'.format(len(X)))
        else:
            erros.append(n)
            print('\t\t---------------------------------------------------')
            print('\t\t    Você ERROU :-(')
            if(contador < 9):
                print('\n\t\t    Faltam {} números para ser um vencedor.\n\t\t    Suas Chances: {}\n\t\t\t    ... Tente novamente...'.format(len(X), (10-(contador+1))))
            contador += 1
    if(contador == 10):
        print('\n\n\t\t---------------------------------------------------')
        print('\t\t\t FIM DE JOGO VOCÊ PERDEU!')
        vitoria = 'DERROTA'
        print('\t\t\t\t Pontuação total: {}/{}'.format(pontos, len(l)))
        print('\t\t---------------------------------------------------')
    elif(contador < 10 and len(X) == 0):
        print('\n\n\t\t---------------------------------------------------')
        print('\t\t\t PARABÉNS! VOCÊ É UM VENCEDOR!')
        vitoria = 'VITÓRIA'
        print('\t\t\t\t Pontuação total: {}/{}'.format(pontos, len(l)))
        print('\t\t---------------------------------------------------')
    with open('lab06_q02_ronivaldo_andrade_(jogo_acerte_numero).log', 'a') as log:
        log.write('\n\t\t\t\tJOGO ACERTE O NÚMERO\n\n')
        hora = datetime.now().strftime('%d/%m/%Y | %H:%M:%S')
        log.write('Data do jogo: {}\n'.format(hora))
        log.write('Lista usada: {}\n'.format(l))
        log.write('Desenvoltura no jogo:\n\t Acertos: {}\n\t Erros:{}\n'.format(acertos, erros))
        log.write('Resultado final:\n\t Potuação: {}/{}\n\t Qantidade de erros: {}/10\n\t Status do jogador: {}\n'.format(pontos, len(l), contador, vitoria))
    r = input('\n\n\t\t Deseja jogar novamente?(ENTER --> sim, N --> não)')
    print('------------------------------------------------------------------------------------\n\n')
    if(r == ''):
        main()
    else:
        quit()
        pass
    pass
if __name__ == '__main__':
    main()
    pass
