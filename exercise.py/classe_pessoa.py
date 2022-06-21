# -*- coding: utf-8 -*-
__author__     = "Ronivaldo Domingues de Andrade"
__course__     = "Engenharia Elétrica - 2º Período"
__university__ = "Universidade Federal do Rio de Janeiro"
__version__    = "1.0"
__date__       = "06/04/2021"
__python__     = "3.7"
# 1) CLASSE PESSOA.
class Pessoa:
    '''Essa é a classe Pessoa, ela cria e manipula os dados de uma pessoa;
    OBS.: Vale ressaltar que a idade de uma pessoa é sempre um inteiro maior que 0(zero)
    E os outros dados a serem inseridoa devem sempre ser em formato de string;'''
    def __init__(self, nome, nome_social, sobrenome, idade, estado_civil):
        '''Esta é a função construtora da classe Pessoa, seu trabalho é criar o objeto e adicionar a ele suas propriedades;
        STR, STR, STR, INT, STR --> NONE'''
        self.nome = nome
        self.nome_social = nome_social
        self.sobrenome = sobrenome
        self.idade = idade
        self.estado_civil = estado_civil
    def setNomeSocial(self, new_social_name):
        '''Essa função permite que o individuo atualize seu nome social nos dados já cadastrados;
        STR --> NONE'''
        if(str.lower(new_social_name) != str.lower(self.nome_social)):
            self.nome_social = new_social_name
    def aniversario(self, birthday):
        '''Essa função permite que o individuo atualize sua idade nos dados já cadastrados, sempre que este fizer aniversário;
        OBS.: Lebrando que esse dado deve sempre ser inserido como um inteiro maior que 0;
        INT --> NONE'''
        if(birthday > self.idade):
            self.idade = birthday
    def setEstadoCivil(self, civil_status):
        '''Essa função permite que o individuo atualize seu nome social nos dados já cadastrados;
        STR --> NONE'''
        if(str.lower(civil_status) != str.lower(self.estado_civil)):
            self.estado_civil = civil_status
            pass
        pass
    pass
# 2) CLASSE PESSOA FÍSICA.
class PessoaFisica(Pessoa):
    '''Essa classe tem por finalidade de, certa forma, implementar a classe Pessoa, pois seu trabalho é pegar os dados já existentes e cadastrados de um individuo
    e completálo com seu CPF e seu RG;
    OBS.: Todos os dados exceto a idade devem ser inseridos com o formato de string;'''
    def __init__(self, nome, nome_social, sobrenome, idade, estado_civil, cpf, rg):
        '''Essa função é o construtor da classe PessoaFisica, ela recebe os atributos já criados na classe Pessoa e os complementa;
        STR, STR, STR, INT, STR, STR, STR --> NONE'''
        Pessoa.__init__(self, nome, nome_social, sobrenome, idade, estado_civil)
        self.cpf = cpf
        self.rg = rg
        pass
    pass
# 3) CLASSE PESSOA JURÍDICA.
class PessoaJuridica(Pessoa):
    '''Essa classe tem por finalidade de, certa forma, implementar a classe Pessoa, pois seu trabalho é pegar os dados já existentes e cadastrados de um individuo
    e completálo com seu CPF e seu RG;
    OBS.: Todos os dados exceto a idade devem ser inseridos com o formato de string;'''
    def __init__(self, nome, nome_social, sobrenome, idade, estado_civil, cnpj):
        '''Essa função é o construtor da classe PessoaJuridica, ela recebe os atributos já criados na classe Pessoa e os complementa;
        STR, STR, STR, INT, STR, STR --> NONE'''
        Pessoa.__init__(self, nome, nome_social, sobrenome, idade, estado_civil)
        self.cnpj = cnpj
        pass
    pass
# 4) CLASSE EMPREGADO.
class Empregado(PessoaFisica):
    '''Essa classe tem por finalidade pegar os dados já existentes na classe PessoaFisica e completálo com seu salario mensal;
    OBS-1.: Todos os dados exceto a idade e o salário devem ser inseridos com o formato de string;
    OBS-2.: O salário que deverá ser informado é mensal;'''
    def __init__(self, nome, nome_social, sobrenome, idade, estado_civil, cpf, rg, salario):
        '''Essa função é o construtor da classe Empregado, ela recebe os atributos já criados na classe PessoaFisica e os complementa;
        STR, STR, STR, INT, STR, STR, STR, FLOAT --> NONE'''
        PessoaFisica.__init__(self, nome, nome_social, sobrenome, idade, estado_civil, cpf, rg)
        self.salario = salario
    def aumento(self, valor):
        '''Essa função tem por trabalho relizar o aumento ou diminuição do salário de certa pessoa;
        INT --> NONE'''
        novo = self.salario+valor
        if(novo<0):
            print('Esse salário não pode reduzir mais')
        else:
            self.salario += valor
    def totalAnal(self):
        '''Essa função calcula o salario liquido anual de uma pessoa(nos 12 meses correntes);
        NONE --> FLOAT'''
        return 12*self.salario
    pass
# 5) CLASSE EMPRESA.
class Empresa(PessoaJuridica):
    '''Essa classe tem por finalidade pegar os dados já existentes e cadastrados de uma empresa e completá-los com seu noem fantasia e seu quadro de funcionários;
    OBS.: Todos os dados exceto a idade e a lista de funcionarios devem ser inseridos com o formato de string;
    OBS.: A LISTA DE FUNCIONARIOS DEVE SER UMA LISTA DE OBJETOS DO TIPO EMPREGADOS COM SEUS SALARIOS ATUAIS'''
    def __init__(self, nome, nome_social, sobrenome, idade, estado_civil, cnpj,nome_fantasia,funcionarios=[]):
        '''Essa função é o construtor da classe Empresa, ela recebe os atributos já criados na classe PessoaJuridica e os complementa;
        STR, STR, STR, INT, STR, STR, STR, LIST --> NONE'''
        PessoaJuridica.__init__(self, nome, nome_social, sobrenome, idade, estado_civil, cnpj)
        self.nome_fantasia = nome_fantasia
        if(type(funcionarios) != list):
            self.funcionarios = []
        else:
            self.funcionarios = funcionarios
    def ContrataFuncionario(self, nome, nome_social, sobrenome, idade, estado_civil, cpf, rg, salario):
        '''Essa função adiciona à lista de funcionarios da empresa um novo funcionário que deverá ser cadastrado e registrado todos os seus dados;
        STR, STR, STR, INT, STR, STR, STR, FLOAT --> NONE'''
        funcionario = Empregado(nome, nome_social, sobrenome, idade, estado_civil, cpf, rg, salario)
        for i in self.funcionarios:
            if(funcionario.cpf == i.cpf):
                print('O funcionário que está tentando cadastrar já trabalha conosco!')
                return None
        self.funcionarios.append(funcionario)
    def showFuncionarios(self):
        '''Essa função tem por objetivo exibir a lista de funcionários da empresa com seus nomes, sobrenomes, cpf e salario atual;
        NONE --> LIST'''
        funcionarios = []
        for elementos in self.funcionarios:
          funcionarios.append((elementos.nome, elementos.sobrenome, elementos.cpf))
        return funcionarios
    def demiteFuncionario(self, cpf):
        '''Essa função recebe o CPF de um funcionario que deverá ser demitido e imediatamente o exclui da lista de funcionários da empresa;
        STR --> NONE'''
        for pessoa in self.funcionarios:
            if cpf == pessoa.cpf:
                self.funcionarios.remove(pessoa)
                return('Foi demitido(a)!')
        print('Essa pessoa não trabalha nesta empresa')
        pass
    pass
