import cherrypy
from classes.Usuarios import *
from pageUsuario import PaginaUsuario

class PaginaLogin():
    nav = open("html/navbar.html",encoding='UTF8').read()
    rodape = open("html/rodape.html",encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.formLogin()

    def formLogin(self,pId=0,pNome='',pEmail = '',pCpf='',pFunc=0,pSenha='',pEndereco=''):

        html = self.nav
        html = html + '''
            <div class="container">
                <div class="divfundo2">
                    <h1 class="titulo">Login</h1>
                    <form name="LoginUsuarios" action="Login" method="post">
                        <label for="tusuario">Usuário (CPF): </label>
                        <br />
                        <input class="box" type="text" id="tusuario" name="tusuario" value="%s" pattern="\d{3}\.\d{3}\.\d{3}-\d{2}"
                            placeholder="xxx.xxx.xxx-xx" required="required" />
                        <br />
                        <label for="tsenha">Senha: </label>
                        <br />
                        <input class="box" type="password" id="tsenha" name="tsenha" size="32" maxlength="12" placeholder="Digite sua senha!"
                            required="required" value="%s"/>
                        <br /><br />
                        <input class="btn-adote" type="submit" id="bgravar" name="bgravar" onclick="return Login()" value="Login" />
                        <input class="btn-adote" type="reset" id="blimpar" value="Limpar" />
                    </form>
                    <p>Não tem uma conta? <a href="/pgCadastrar">Registre-se aqui.</a></p>
                </div>
            </div>
        ''' % (pEmail, pSenha)

        html = html + self.rodape

        return html

    @cherrypy.expose()
    def Login(self,tusuario,tsenha,bgravar):

        objUsu = Usuarios()
        dados = objUsu.obterUsuarioLogin(tusuario)
        if dados[0]["usu_senha"] == tsenha:
            raise cherrypy.HTTPRedirect("/pgUsuario")
        else:
            return '''
                <script>
                     alert("Favor informar senha correta!");
                </script>
            '''