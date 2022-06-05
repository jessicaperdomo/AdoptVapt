import cherrypy
from classes.Usuarios import *


class PaginaUsuario():
    nav = open("html/navbar.html", encoding='UTF8').read()
    rodape = open("html/rodape.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.UsuarioP()

    @cherrypy.expose()
    def UsuarioP(self,pId=1):
        html = self.nav
        html = html + self.formAltera(pId)
        html = html + self.rodape
        return html

    def formAltera(self,pId):
        objUsu = Usuarios()
        objUsu.set_id(pId)
        dados = objUsu.obterUsuario(pId)

        html = '''
                            <div class="caixa">
                                <div class="divfundo">
                                    <h1 class="titulo">Alterando Usuário</h1>
                                    <form name="FormCad" action="alterarUsuario" method="post">
                                        <input type="hidden" id="txtId" name="txtId" value="%s" />
                                        <label for="tnome">Nome: </label>
                                        <br />
                                        <input class="box" type="text" id="tnome" name="tnome" value="%s" size="40" maxlength="35" placeholder="Digite seu nome"
                                            required="required" >
                                        <br />
                                        <label for="temail">E-mail: </label>
                                        <br />
                                        <input class="box" type="email" id="temail" name="temail" value="%s" size="40" placeholder="modelo123@exemplo.com"
                                            required="required" />
                                        <br />
                                        <input type="hidden" id="tsenha" name="tsenha" value="%s" />
                                        <input type="hidden" id="tcpf" name="tcpf" value="%s" />
                                        <label for="tendereco">Endereço: </label>
                                        <br />
                                        <input class="box" type="text" id="tendereco" name="tendereco" value="%s" size="36" maxlength="35"
                                            placeholder="Digite seu endereço" required="required">
                                        <br />
                                        <input class="btn-adote" type="submit" id="bgravar" name="bgravar" onclick=alterarUsuario() value="Alterar" />
                                        <input class="btn-adote" type="reset" id="blimpar" value="Limpar" />
                                    </form>
                                </div>
                            </div>
                ''' % (dados[0]["usu_id"], dados[0]["usu_nome"], dados[0]["usu_email"], dados[0]["usu_senha"],dados[0]["usu_cpf"], dados[0]["usu_endereco"])

        return html

    @cherrypy.expose()
    def alterarUsuario(self,tcpf,bgravar):
        objUsu = Usuarios()
        objUsu.set_cpf(tcpf)
        dados = objUsu.obterUsuarioLogin(tcpf)
        return self.UsuarioP(dados[0]["usu_id"], dados[0]["usu_nome"], dados[0]["usu_email"],dados[0]["usu_senha"],dados[0]["usu_cpf"],dados[0]["usu_endereco"])