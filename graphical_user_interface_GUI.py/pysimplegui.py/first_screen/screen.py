import PySimpleGUI as psg

class ScreenPSG():
    def __init__(self) -> None:
        '''Essa função cria toda a tela e assim que pedimos a ela, a tela gerada é mostrada'''
        
        psg.change_look_and_feel('DarkBrown4')
        
        layout = [
            [psg.Text('Nome', size=(5,1)), psg.Input(size=(30,1), key='nome')],
            [psg.Text('Idade', size=(5,1)), psg.Input(size=(30,1), key='idade')],
            [psg.Text('Quais provedores de e-mail são aceitos?')],
            [psg.Checkbox('Gmail', key='gmail'), psg.Checkbox('Outlook', key='outlook'), psg.Checkbox('Yahoo', key='yahoo')],
            [psg.Text('Aceita Cartão?')],
            [psg.Radio('Sim', 'cartoes', key='aceita'), psg.Radio('Não', 'cartoes', key='naoaceita')],
            [psg.Slider(range=(0,100), default_value=10, orientation='h', size=(20,15), key='velocidade'), psg.Slider(range=(0,200), default_value=50, orientation='v', size=(5,15),key='velocidade2')],
            [psg.Button('Enviar Dados')],
            [psg.Output(size=(40,10))]
            ]
        
        self.window = psg.Window('Dados do Usuário').layout(layout)
        pass
    
    def start(self) -> None:
        '''Essa função além de inicializar a tela e a exibir ele também a mantém aberta e coletando os dados inseridos pelo usuário continuamente;'''
        
        while True:
            
            self.button, self.values = self.window.Read()
            
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

if __name__ == "__main__":
    window = ScreenPSG()
    window.start()
    pass
