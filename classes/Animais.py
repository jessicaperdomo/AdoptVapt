from classes.BancoD import *

class Animais():

    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__foto = ''
        self.__cpf = ''
        self.__sexo = 0
        self.__porte = 0
        self.__tipo = 0
        self.__desc = ''
        self.__banco = BancoD()

    def set_id(self, pId):
        if pId > 0:
            self.__id = pId

    def set_nome(self, pNome):
        if len(pNome) > 0:
            self.__nome = pNome

    def set_foto(self, pFoto):
        if len(pFoto) > 0:
            self.__foto = pFoto

    def set_cpf(self, pCpf):
        if len(pCpf) > 0:
            self.__cpf = pCpf

    def set_sexo(self, pSexo):
        if pSexo > 0:
            self.__sexo = pSexo

    def set_porte(self, pPorte):
        if pPorte > 0:
            self.__porte = pPorte

    def set_tipo(self, pTipo):
        if pTipo > 0:
            self.__tipo = pTipo

    def set_desc(self, pDesc):
        if len(pDesc) > 0:
            self.__desc = pDesc

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_foto(self):
        return self.__foto

    def get_cpf(self):
        return self.__cpf

    def get_sexo(self):
        return self.__sexo

    def get_porte(self):
        return self.__porte

    def get_tipo(self):
        return self.__tipo

    def get__desc(self):
        return self.__desc

    def gravar(self):
        sql = "insert into Animais (ani_nome,ani_foto,ani_cpf,ani_sexo,ani_porte,ani_tipo,ani_desc) " \
              "values ('#nome','#foto','#cpf',#sexo,#porte,#tipo,'#desc')"

        sql = sql.replace("#nome", self.__nome)
        sql = sql.replace("#foto", self.__foto)
        sql = sql.replace("#cpf", self.__cpf)
        sql = sql.replace("#sexo", str(self.__sexo))
        sql = sql.replace("#porte", str(self.__porte))
        sql = sql.replace("#tipo", str(self.__tipo))
        sql = sql.replace("#desc", self.__desc)

        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        try:
            sql = "update Animais set ani_nome = '#nome',ani_foto = '#foto',ani_cpf = '#nro',ani_sexo = #sexo,ani_porte = #port,ani_tipo = #tip" \
                  "where ani_id = #id"

            sql = sql.replace('#id', str(self.__id))
            sql = sql.replace("#nome", self.__nome)
            sql = sql.replace("#foto",self.__foto)
            sql = sql.replace("#nro", self.__cpf)
            sql = sql.replace("#sexo", str(self.__sexo))
            sql = sql.replace("#port", str(self.__porte))
            sql = sql.replace("#tip", str(self.__tipo))

            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def excluir(self):
        try:
            sql = "delete from Animais where ani_id = #id"
            sql = sql.replace('#id', str(self.__id))
            return self.__banco.executarInsertUpdateDelete(sql)
        except:
            return -1

    def obterAnimal(self, id = 0):
        if id != 0:
            self.__id = id
        sql = "select ani_id,ani_nome,ani_foto,ani_cpf,ani_sexo,ani_porte,ani_tipo,ani_desc from Animais where ani_id = #id"
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    def obterTodosAnimais(self):
        sql = "select ani_id, ani_nome,ani_foto,ani_cpf,ani_sexo,ani_porte,ani_tipo,ani_desc from Animais order by ani_nome"
        return self.__banco.executarSelect(sql)

    def obterTodosAnimaisC(self):
        sql = "select ani_nome,ani_foto,ani_cpf,ani_desc,se_nome,tip_nome,por_nome from Animais, Sexo_animal, Tipos_animal,Porte_Animal" \
              "where (Animais.ani_sexo = Sexo_animal.se_id),(Animais.ani_tipo = Tipos_animal.tip_id),(Animais.ani_porte = Porte_animal.por_id)"
        return self.__banco.executarSelect(sql)