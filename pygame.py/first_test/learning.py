# Importando as bibliotecas necessárias para criar um jogo.
import pygame
from pygame.locals import *

# Inicializando o pygame.
pygame.init()

# Criando a tela do jogo com as dimensões que desejamos.
screen = pygame.display.set_mode((1280, 640))

# Dando um titulo personalizado a janela.
pygame.display.set_caption('Meu primeiro Jogo')

# Definindo o icone que aparecerá na janela do jogo.
#pygame.display.set_icon()

# Criando o loop infinito principal do jogo
while True:
    # Criando o coletador de eventos vindos da janela do jogo.
    for event in pygame.event.get():
        # Filtrando o evento do tipo QUIT que é aquele quando o jogador clica com o mouse no (X) da janela.
        if event.type == pygame.QUIT:
            pygame.quit()
            # Forçando todo o jogo a parar.
            exit()
    # Comando que fará a janela sempre atualisar em cada vez que passa pelo loop (Normalmente é a ultima coisa que vem no código).
    pygame.display.flip()

