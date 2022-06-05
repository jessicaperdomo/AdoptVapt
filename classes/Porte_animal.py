from classes.BancoD import *

class Porte_Animal():

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
        sql = "insert into porte_animal (por_nome) " \
              "values ('#nome')"

        sql = sql.replace("#nome", self.__nome)
        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        try:
            sql = "update porte_animal set por_nome = '#nome'" \
                  "where por_id = #id"
            sql = sql.replace("#nome", self.__nome)
            sql = sql.replace('#id', str(self.__id))

            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def excluir(self):
        try:
            sql = "delete from porte_animal where por_id = #id"
            sql = sql.replace('#id', str(self.__id))
            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def obterTipo(self, id=0):
        if id != 0:
            self.__id = id
        sql = "select por_id, por_nome from porte_animal where por_id = #id"
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    def obterTipos(self):
        sql = "select por_id, por_nome from porte_animal order by por_nome"
        return self.__banco.executarSelect(sql)