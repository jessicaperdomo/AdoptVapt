import cherrypy
from classes.Usuarios import *


class PaginaCadastro():
    nav = open("html/navbar.html", encoding='UTF8').read()
    rodape = open("html/rodape.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.FormCad()

    def FormCad(self, pId=0, pNome='', pEmail='', pCpf='', pSenha='', pEndereco=''):
        html = self.nav
        html = html + '''
            <div class="caixa">
                <div class="divfundo">
                    <h1 class="titulo">Cadastro de Usuário</h1>
                    <form name="FormCad" action="gravarUsuario" method="post">
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
                        <label for="tsenha">Defina uma senha de acesso: </label>
                        <br />
                        <input class="box" type="password" id="tsenha" name="tsenha" value="%s" size="22" maxlength="12" placeholder="Letras e números"
                            required="required" />
                        <br />
                        <label for="tcpf">Digite seu CPF: </label>
                        <br />
                        <input class="box" type="text" id="tcpf" name="tcpf" value="%s" pattern="\d{3}\.\d{3}\.\d{3}-\d{2}"
                            placeholder="xxx.xxx.xxx-xx" required="required" />
                        <br />
                        <label for="tendereco">Endereço: </label>
                        <br />
                        <input class="box" type="text" id="tendereco" name="tendereco" value="%s" size="36" maxlength="35"
                            placeholder="Digite seu endereço" required="required">
                        <br />
                        <input class="btn-adote" type="submit" id="bgravar" name="bgravar" value="Gravar" />
                        <input class="btn-adote" type="reset" id="blimpar" value="Limpar" />
                    </form>
                    <p class="margem">Já tem uma conta? <a href="/pageLogin">Faça o login aqui.</a></p>
                </div>
            </div>
        ''' % (pId,pNome,pEmail,pSenha,pCpf,pEndereco)

        html = html + self.rodape
        return html

    @cherrypy.expose()
    def gravarUsuario(self, txtId, tnome, temail, tsenha, tcpf, tendereco, bgravar):

        if len(tnome) > 0:
            objUsu = Usuarios()
            objUsu.set_nome(tnome)
            objUsu.set_email(temail)
            objUsu.set_senha(tsenha)
            objUsu.set_cpf(tcpf)
            objUsu.set_endereco(tendereco)
            retorno = 0

            if int(txtId) == 0:
                retorno = objUsu.gravar()
            else:
                objUsu.set_id(int(txtId))
                retorno = objUsu.alterar()

            if retorno > 0:
                return '''
                        <script>
                            alert("Usuario cadastrado com sucesso!");
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
                        alert("Nome do usuario precisa ser informado!");
                    </script>
                '''
