import cherrypy
from classes.Animais import *


class PaginaCaodastro():
    nav = open("html/navbar.html", encoding='UTF8').read()
    rodape = open("html/rodape.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.FormCaod()

    def FormCaod(self, pId=0, pNome='',pFoto='',pCpf='',pSexo=0,pPorte=0,pTipo=0,pDesc=''):
        html = self.nav
        html = html + '''
            <div class="container">
                <div class="divfundo">
                    <h1 class="titulo">Cãodastro de Pets</h1><br>
                    <form name="FCadastro" action="gravarAnimal" method="post">
                    
                        <input type="hidden" id="txtId" name="txtId" value="%s" />
                        
                        <label for="nome">Digite o Nome do Pet</label><br>
                        <input class="box" type="text" id="tnome" name="tnome" value="%s" size="40" maxlength="35" placeholder="Digite seu nome"
                            required="required" />
                        
                        <br />
                        <label for="ftpet">Selecione uma Foto do Pet!<label><br>
                        <input class="box" type="text" id="ftpet" name="ftpet" value="%s" size="40" placeholder="Nome do arquivo" />
                        <br />
                        
                        <label for="tcpf">Digite o cpf de usuário<label><br>
                        <input class="box" type="text" id="tcpf" name="tcpf" value="%s" size="40" maxlength="35" placeholder="Digite seu cpf"
                            required="required"/>
                        <br />
                        
                        <label for="sexpet">Qual o Sexo do Pet ?</label>
                        <br />
                        <input type="radio" id="sexpet" name="sexpet" value="1" />
                        <label for="sexpet1">Fêmea</label>
                        
                        <input type="radio" id="sexpet" name="sexpet" value="2" />
                        <label for="sexpet2">Macho</label>
                        
                        <br />
                        <label for="portpet">Qual o Porte do Pet ?</label>
                        <br />
                        <input type="radio" id="portpet" name="portpet" value="1" />
                        <label for="portpet1">Pequeno</label>
    
                        <input type="radio" id="portpet" name="portpet" value="2" />
                        <label for="portpet2">Médio</label>
        
                        <input type="radio" id="portpet" name="portpet" value="3" />
                        <label for="portpet3">Grande</label>
                        <br />
                        
                        <label for="qlpet">Qual o Pet ?</label>
                        <br />
                        <input type="radio" id="qlpet" name="qlpet" value="1" />
                        <label for="qualpet1">Cão</label>
                        <input type="radio" id="qlpet" name="qlpet" value="2" />
                        <label for="qualpet2">Gato</label>
                        <input type="radio" id="qlpet" name="qlpet" value="3" />
                        <label for="qualpet3">Tartaruga</label>
                        <input type="radio" id="qlpet" name="qlpet" value="4" />
                        <label for="qualpet4">Passarinho</label>
                        <br />
        
                        <label for="petdesc">Descreva seu Pet !</label>
                        <br />
                        <input class="box" class="textarea" type="text" id="descpet" name="descpet" value="%s" size="50" placeholder="Ele(a) adora brincar!"/>
                        <br />
                        
                        <input class="btn-adote" type="submit" id="bgravar" name="bgravar" value="Gravar" />
                        <input class="btn-adote" type="reset" id="blimpar" value="Limpar" />
                    </form>
                </div>
            </div>
        ''' % (pId, pNome, pFoto,pDesc,pCpf)

        html = html + self.rodape
        return html

    @cherrypy.expose()
    def gravarAnimal(self, txtId, tnome,ftpet,tcpf,sexpet,portpet,qlpet,descpet, bgravar):
        if len(tnome) > 0:
            objAni = Animais()
            objAni.set_nome(tnome)
            objAni.set_tipo(int(qlpet))
            objAni.set_sexo(int(sexpet))
            objAni.set_porte(int(portpet))
            objAni.set_foto(ftpet)
            objAni.set_desc(descpet)
            objAni.set_cpf(tcpf)
            retorno = 0

            if int(txtId) == 0:
                retorno = objAni.gravar()
            else:
                objAni.set_id(int(txtId))
                retorno = objAni.alterar()

            if retorno > 0:
                return '''
                       <script>
                            alert("Animal cadastrado com sucesso!");
                        </script>
                    '''
            else:
                return '''
                        <script>
                            alert("Erro ao salvar usuario!");
                        </script>
                    '''
        else:
            return '''  
                    <script>
                        alert("Nome do animal precisa ser informado!");
                    </script>
                '''

