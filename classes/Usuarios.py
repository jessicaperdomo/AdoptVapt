from classes.BancoD import *

class Usuarios():
    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__email = ''
        self.__cpf = ''
        self.__senha = ''
        self.__endereco = ''
        self.__banco = BancoD()

    def set_id(self, pId):
        if pId > 0:
            self.__id = pId

    def set_nome(self, pNome):
        if len(pNome) > 0:
            self.__nome = pNome

    def set_email(self, pEmail):
        if len(pEmail) > 0:
            self.__email = pEmail

    def set_cpf(self, pCpf):
        if len(pCpf) > 0:
            self.__cpf = pCpf

    def set_senha(self, pSenha):
        if len(pSenha) > 0:
            self.__senha = pSenha

    def set_endereco(self, pEndereco):
        if len(pEndereco) > 0:
            self.__endereco = pEndereco

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_cpf(self):
        return self.__cpf

    def get_senha(self):
        return self.__senha

    def get_endereco(self):
        return self.__endereco

    def gravar(self):
        sql = "insert into Usuarios (usu_nome,usu_email,usu_cpf,usu_senha,usu_endereco) " \
              "values ('#nome','#email','#cpf','#senha','#endereco')"
        sql = sql.replace("#nome", self.__nome)
        sql = sql.replace("#email", self.__email)
        sql = sql.replace("#cpf", self.__cpf)
        sql = sql.replace("#senha", self.__senha)
        sql = sql.replace("#endereco", self.__endereco)

        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        try:
            sql = "update Usuarios set usu_nome = '#nome', usu_email = '#email', usu_cpf = '#cpf', usu_senha = '#senha', usu_endereco = '#endereco'" \
                  "where usu_id = #id"

            sql = sql.replace("#id", str(self.__id))
            sql = sql.replace("#nome", self.__nome)
            sql = sql.replace("#email", self.__email)
            sql = sql.replace("#cpf", self.__cpf)
            sql = sql.replace("#senha", self.__senha)
            sql = sql.replace("#endereco", self.__endereco)

            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def excluir(self):
        try:
            sql = "delete from Usuarios where usu_id = #id"
            sql = sql.replace('#id', str(self.__id))

            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def obterUsuario(self, id = 0):
        if id != 0:
            self.__id = id

        sql = "select usu_id,usu_nome,usu_email,usu_cpf,usu_senha,usu_endereco from Usuarios where usu_id = #id"
        sql = sql.replace('#id', str(self.__id))

        return self.__banco.executarSelect(sql)

    def obterUsuarioLogin(self, cpf=''):
        if len(cpf) > 0:
            self.__cpf = cpf

        sql = "select usu_id,usu_nome,usu_email,usu_cpf,usu_senha,usu_endereco from Usuarios where usu_cpf = '#cpf'"
        sql = sql.replace("#cpf", self.__cpf)

        return self.__banco.executarSelect(sql)

    def obterTodosUsuarios(self):
        sql = "select usu_id,usu_nome,usu_email,usu_cpf,usu_senha,usu_endereco from Usuarios order by usu_nome"
        return self.__banco.executarSelect(sql)