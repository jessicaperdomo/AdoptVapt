import cherrypy
import os

from pageLogin import PaginaLogin
from pageCadastro import PaginaCadastro
from pageCaodastro import PaginaCaodastro
from pageAnimais import PaginaAnimais
from pageSobrePortfolios import PaginaSobre
from pageUsuario import PaginaUsuario
from pagePortArt import PaginaPortArthur
from pagePortJean import PaginaPortJean
from pagePortJess import PaginaPortJess
from pagePortYuri import PaginaPortYuri
from pageAnimalDet import PaginaAnimaisDetalhes

local_dir = os.path.dirname(__file__)

class PaginaHome():
    nav = open("html/navbar.html",encoding='UTF8').read()
    rodape = open("html/rodape.html",encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        html = self.nav
        html = html + '''
            <section class="sec-img">
                <div class="imagem-inicial">
                    <img src="../assets/Frase.png" alt="Todos merecem um lar">
                </div>
            </section>
        '''
        html = html + self.rodape

        return html

server_config = {
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 81,
}

cherrypy.config.update(server_config)

local_config = {
    "/":{"tools.staticdir.on": True,
          "tools.staticdir.dir": local_dir},
}

root = PaginaHome()
root.pageLogin = PaginaLogin()
root.pgCadastrar = PaginaCadastro()
root.pgCaodastrar = PaginaCaodastro()
root.pgAnimais = PaginaAnimais()
root.pgSobre = PaginaSobre()
root.pgUsuario = PaginaUsuario()
root.pgPortArt = PaginaPortArthur()
root.pgPortJean = PaginaPortJean()
root.pgPortJess = PaginaPortJess()
root.pgPortYuri = PaginaPortYuri()
root.pageAnis = PaginaAnimaisDetalhes()

cherrypy.quickstart(root, config=local_config)
