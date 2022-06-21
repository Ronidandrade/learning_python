# -*- coding: utf-8 -*-

__author__     = "Ronivaldo Domingues de Andrade"
__course__     = "Engenharia Elétrica - 2º Período"
__university__ = "Universidade Federal do Rio de Janeiro"
__version__    = "2.0"
__date__       = "25/05/2021"
__python__     = "3.9"

# Importando as bibliotecas necessárias.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1) Plotando um gráfico de disperção.

def g_dispersao()->None:
    ''' A fução const´roi e plota um grafico de disperção baseado nos dados capturados de um arquivo .csv'''

    # Fazendo a leitura do arquivo '.csv' exeterno.
    db = pd.read_csv(r".\lab09_dados_ronivaldo_andrade.csv")

    # Colocando o arquivo em ordem decrescente de valores com relação aos valores da coluna "area".
    db = db.sort_values(by="area", ascending=False)

    # Criando um novo DataFrame com as primeiras 300 linhas do DataFrame 'db' e como ele foi ordenado de forma decrescente esses são os maiores valores
    # relacionados as areas.
    ndb = db.head(300)

    # Separando os nomes dos bairros dos dados brutos e com isso criando um array linha.
    bairros = ndb['bairro'].unique()
    
    ## Essa lista salvará os DataFrame referente a cada um dos bairros listados em 'bairros'.
    lb = []

    ## Este for pega o DataFrame 'ndb' e filtra novos DataFrames, os quais apenas possuem os bairros desejados e os armazena na lista 'lb'.
    for bairro in bairros:
        lb.append(ndb[ndb['bairro'] == bairro])
        pass

    # Construndo o Gráfico de Dispersão.
    ## Definindo o formato e o estilo do grafico.
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6.9,5.14))

    # Plotando os dados.
    ## Elencando as cores que serão distribuidas entre os diferentes bairros para representá-los.
    color = ['r','g','b','c','m','y','k']

    ## O for percorre a lista de DataFrames dos bairros 'lb'.
    for i in range(len(lb)):
        ## Aqui o 'color=color[i]' dentro do for vai pintar cada bairro de uma cor, e quando passar da primeira iteração, o 'i' aumentará e a cor não mais será usada.
        ## A mesma coisa funciona para 'label', como 'lb' foi criado a partir de 'bairros' e cada DataFrame em 'lb' corresponde diretamente a cada bairro em bairros
        ## quando 'i' for o primeiro DataFrame em 'lb' ele também será o primeiro bairro em 'bairros' o que faz que para cada linha e cada bolinha correspondente
        ## ao DataFrame seja inserida a mesma cor e o mesmo label.
        ## Com relação a transparência apliquei a mesma a todos.
        lb[i].plot.scatter(ax=ax,x='area', y='condominio', s=(lb[i]['preco'])/40300, color=color[i], label=bairros[i], alpha=0.6)
        pass

    # Incluindo o titulo do gráfico.
    ax.set_title('Área X valor do condomínio de apartamentos no Rio de Janeiro')

    # Incluindo rótulo nos eixos.
    plt.xlabel(r'Área $m^2$')
    plt.ylabel('Condomínio')
    
    # Incluindo a Legenda.
    ax.legend(loc="lower right")
    
    # Exibindo o grafico para o usuario.
    plt.show()
    pass

if __name__ == '__main__':
    g_dispersao()
    pass
