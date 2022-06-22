1. Importando a biliotecas necessárias para a criação dessa tela, nesse caso apenas a biblioteca PySimpleGUI.  
1.1. Ao importar daremos ao pacote um apelido(alias) para que ele fique mais fácil de chamar(referênciar) durante a sua utilização no programa.

```python
import PySimpleGUI as psg

#Criaremos uma Classe para armazenar toda a janela e suas configurações.

class ScreenPSG():
    def __init__(self) -> None:
        '''Essa função cria toda a tela e assim que pedimos a ela, a tela gerada é mostrada'''
        
        # Para alterar o estilo da tela basta olhar a tabela e ir alterando a string dentro do comando abaixo.
        psg.change_look_and_feel('DarkBrown4')
        
        # Usando o apelido (psg) acessaremos os modulos/métodos (Text, Input, Button) da biblioteca para criar os objetos de interação na tela.
        ## Veja que aqui a ordem importa, funciona igual ao HTML se trocar a ordem dos campos dentro da lista abaixo eles trocam de ordem na impressão da tela.
        ### O parâmetro size=(x,y) indica o tamanho que a figura vai ter ao renderizar, X e Y são em quantidade de caracteres por linha e coluna respectivamente.
        ### O parâmetro key="chave" faz com que na hora de coletar os dados da tela fique mais facil navegar por eles.
        layout = [
            [psg.Text('Nome', size=(5,1)), psg.Input(size=(30,1), key='nome')],
            [psg.Text('Idade', size=(5,1)), psg.Input(size=(30,1), key='idade')],
            [psg.Text('Quais provedores de e-mail são aceitos?')],
            [psg.Checkbox('Gmail', key='gmail'), psg.Checkbox('Outlook', key='outlook'), psg.Checkbox('Yahoo', key='yahoo')],
            [psg.Text('Aceita Cartão?')],
            
            ### Aqui devemos referenciar a qual Label pertence as opções do radio button, nesse caso pertece ao cartoes, se não referenciar,
            ### ele pode acabar permitindo selecionar dois ao mesmo tempo, o que não deveria acontecer com os botões radio.
            [psg.Radio('Sim', 'cartoes', key='aceita'), psg.Radio('Não', 'cartoes', key='naoaceita')],
            [psg.Slider(range=(0,100), default_value=10, orientation='h', size=(20,15), key='velocidade'), psg.Slider(range=(0,200), default_value=50, orientation='v', size=(5,15),key='velocidade2')],
            [psg.Button('Enviar Dados')],
            
            ### O botão Output pega as infomações inseridas pelo usuario na tela e as mostra dentro de seu campo apenas usando o comando PRINT(), mas
            ### precisamos formatá-las para melhorar a visualização, caso contrário ele apenas mostra um dicionário.
            [psg.Output(size=(40,10))]
            ]
        
        ## Novamente usando o apelido (psg) criaremos a tela que irá exibir o conteúdo, passando o título da janela dentro do comando e atribuindo a ela o layout criando na lista acima
        self.window = psg.Window('Dados do Usuário').layout(layout)
        pass
    
    def start(self) -> None:
        '''Essa função além de inicializar a tela e a exibir ele também a mantém aberta e coletando os dados inseridos pelo usuário continuamente;'''
        
        # Como nos jogos para que a janela não feche após a primeira ação, colocamos um loop infinito e ela pemanecerá aberta até que a fechemos manualmente.
        while True:
            
            ## Chamamos os atributos do (psg) para coletar as ações e informações digitados nos campos da tela criada e os salva em dicionário.
            self.button, self.values = self.window.Read()
            
            ### Atribuindo à variáveis os dados inseridos pelo usúario.
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceita']
            nao_aceita_cartao = self.values['naoaceita']
            velocidade1 = self.values['velocidade']
            velocidade2 = self.values['velocidade2']
            print(f'Nome: {nome}', f'Idade: {idade}', f'Aceita Gmail: {aceita_gmail}', f'Aceita Outlook: {aceita_outlook}', f'Aceita Yahoo: {aceita_yahoo}', f'Aceita Cartão: {aceita_cartao}', f'Não Aceita Cartão: {nao_aceita_cartao}', f'Velocidades: {velocidade1} e {velocidade2}', sep='. \n', end='\n\n')
            pass
        pass
    pass

# Ciondicional que inicializa o programa dentro das boas práticas de programação.
if __name__ == "__main__":
    window = ScreenPSG()
    window.start()
    pass
```
