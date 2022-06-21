# -*- coding: utf-8 -*-
__author__     = "Ronivaldo Domingues de Andrade";
__course__     = "Engenharia Elétrica - 2º Período";
__university__ = "Universidade Federal do Rio de Janeiro";
__version__    = "1.0";
__date__       = "01/04/2021";
__python__     = "3.7";
# CLASSE PILHA
class Pilha:
    def __init__(self, elementos = []):
        '''Esta é a função construtora da classe Pilha, seu trabalho é criar o objeto e adicionar a ele as suas propriedades;
        LIST --> NONE'''
        if(type(elementos) == list):
            self.elementos = elementos[::]
            print(str.format('Sucesso! | A Pilha armazenada é: {}', self.elementos))
        else:
            self.elementos = []
            print(str.format('Falhou! | A Pilha armazenada é: {}', self.elementos))
    def empilhar(self, elemento):
        '''Essa função faz o empilhamnto dos dados fornecidos, ou seja ao receber um elemento ela o coloca no topo da pilha sobre o último elemento já inserido;
        ELEMENTO --> NONE'''
        self.elementos.append(elemento)
    def desempilhar(self):
        '''Essa função faz o desempilhamento da Pilha, ou seja se houver elementos a serem removidos na pilha, essa função o removerá, do topo da pilha até sua base;
        NONE --> ELEMENTO/NONE'''
        if(len(self.elementos) > 0):
            return(self.elementos.pop())
        else:
            print('Atenção! Pilha sem elementos para desempilhar!')
    def getPilha(self):
        '''Essa função tem o papel de retornar uma cópia dos dados empilhados na Pilha;
        NONE --> LIST'''
        return self.elementos[::]
    def lenPilha(self):
        '''Essa função tem por objetivo contar e retornar o número de elementos/dados que estão na Pilha;
        NONE --> INT'''
        return len(self.elementos)
    def __add__(self, other):
        '''Essa função funciona ao chamar a operação de soma(+), ao tentar somar dois elementos da classe Pilha essa função será usada e deverá realizar essa soma,
        basicamente essa soma consiste em pegar os elementos empilhados na segunda Pilha e colocá-los sobre a primeira Pilha, VEJA que aqui a ordem na operação é muito
        importante, pois sendo p1 e p2 Pilhas distintas p1 + p2 É DIFERENTE DE p2 + p1, não seguindo a propriedade de associatividade da soma comum dos reais;
        PILHA, PILHA --> PILHA'''
        if(type(self.getPilha() == list) and type(other.getPilha() == list)):
            return Pilha((self.getPilha() + other.getPilha()))
        pass;
    pass;
# TESTANDO A CLASSE CRIADA.
def testando():
    '''Essa função irá testar a nossa classe assim que o módulo for rodado no shell;
    NONE --> NONE'''
    print('====================================================================================================================================================')
    print('\t- Criando as instâncias de Pilha p1 e p2:\n\t- É esperado:\n\t\t* Sucesso! | A pilha armazenada é: [1,7,9]\n\t\t* Sucesso! | A pilha armazenada é: []')
    print('\t--------------------------------------------------------------')
    p1 = Pilha([1,7,9])
    p2 = Pilha()
    print('====================================================================================================================================================')
    print('\t- Criando uma instancia p3 com um parâmetro inteiro e testando para ver se o objeto criado é uma instancia de Pilha:\n\t- É esperado:\n\t\t* Falhou! | A pilha armazenada é: []\n\t\t* True')
    print('\t--------------------------------------------------------------')
    p3 = Pilha(3)
    print(isinstance(p3,Pilha))
    print('====================================================================================================================================================')
    print('\t- Empilhar os elementos 4 e 10, nessa ordem, na instância p2 em seguida verificando se os mesmos estão realmente dentro da pilha:\n\t- É esperado:\n\t\t* [4,10]')
    print('\t--------------------------------------------------------------')
    p2.empilhar(4)
    p2.empilhar(10)
    print(p2.getPilha())
    print('====================================================================================================================================================')
    print('\t- Desempilhar os elementos 10 e 4, nessa ordem, na instância p2 em seguida verificando se os mesmos foram realmente desempilhados nessa ordem e efetuar o desempilhamento até aparecer a mensagem de pilha vazia:\n\t- É esperado:\n\t\t* 10\n\t\t* 4\n\t\t* Atenção! Pilha sem elementos para desempilhar!')
    print('\t--------------------------------------------------------------')
    print(p2.desempilhar())
    print(p2.desempilhar())
    p2.desempilhar()
    print('====================================================================================================================================================')
    print('\t- Empilhando o elemento 5 na instância p2:\n\t- É esperado: NADA!')
    p2.empilhar(5)
    print('====================================================================================================================================================')
    print('\t- Criando p4 através da soma de p2 e p1 de modo que p2 fique na base de p4 e verificando se os elemenos estão corretamente empilhados em p4.\n\tEm seguida criando p5 a partir de p2 e p1 de modo que p1 fique na base de p4 e verificando se foi efetuado corretamente:\n\t- É esperado:\n\t\t* Sucesso! | A pilha armazenada é: [5,1,7,9]\n\t\t* [5,1,7,9]\n\t\t* Sucesso! | A pilha armazenada é: [1,7,9,5]\n\t\t* [1,7,9,5]')
    print('\t--------------------------------------------------------------')
    p4 = p2 + p1
    print(p4.getPilha())
    p5 = p1 + p2
    print(p5.getPilha())
    print('====================================================================================================================================================')
    print('\t- Verificando o número de elementos empilhados em p4 e se é igual a quantidade de elemtos de p5:\n\t- É esperado:\n\t\t* 4\n\t\t* True')
    print('\t--------------------------------------------------------------')
    print(p4.lenPilha())
    print(p4.lenPilha() == p5.lenPilha())
    print('====================================================================================================================================================')
    print('\t\t\t\tVERIFICAÇÃO FINALIZADA!')
    pass;
#INICIANDO OS TESTES AUTOMÁTICOS.
if __name__ == '__main__':
    testando()
