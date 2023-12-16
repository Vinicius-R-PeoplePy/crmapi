class Aluno():
    def __init__(self, nome, profissao, situacao, email):
        self.__nome = nome
        self.__profissao = profissao
        self.__situacao = situacao
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao

    @property
    def email(self, email):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
