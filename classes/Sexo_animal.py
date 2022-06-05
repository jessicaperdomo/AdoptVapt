from classes.BancoD import *

class Sexo_Animal():

    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__banco = BancoD()

    def set_id(self, pId):
        if pId > 0:
            self.__id = pId

    def set_nome(self, pNome):
        if len(pNome) > 0:
            self.__nome = pNome

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def gravar(self):
        sql = "insert into sexo_animal (se_nome) " \
              "values ('#nome')"

        sql = sql.replace("#nome", self.__nome)
        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        try:
            sql = "update sexo_animal set se_nome = '#nome'" \
                  "where se_id = #id"
            sql = sql.replace("#nome", self.__nome)
            sql = sql.replace('#id', str(self.__id))

            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def excluir(self):
        try:
            sql = "delete from sexo_animal where se_id = #id"
            sql = sql.replace('#id', str(self.__id))
            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def obterSexo(self, id = 0):
        if id != 0:
            self.__id = id
        sql = "select se_id, se_nome from sexo_animal where se_id = #id"
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    def obterSexos(self):
        sql = "select se_id, se_nome from sexo_animal order by se_nome"
        return self.__banco.executarSelect(sql)