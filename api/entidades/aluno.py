class Aluno():
    def __init__(self, nome, data_nascimento, id_curso):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__id_curso = id_curso

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def id_curso(self):
        return self.__id_curso

    @id_curso.setter
    def id_curso(self, id_curso):
        self.__id_curso = id_curso
