import cherrypy
from classes.Animais import *

class PaginaAnimaisDetalhes():
    nav = open("html/navbar.html", encoding='UTF8').read()
    rodape = open("html/rodape.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.conhecaAni()

    @cherrypy.expose()
    def conhecaAni(self,pId):
        html = self.nav

        html = html + self.criaDetalhes(pId)

        html = html + self.rodape
        return html

    @cherrypy.expose()
    def criaDetalhes(self, pId):
        objAni = Animais()
        dados = objAni.obterAnimal(pId)

        html = '''
                       <section class="beca-sec">
                            <div class="sobre-beca">
                                <img class="img-sobre" src="/assets/%s" alt="%s %s">
                                <div class="infos-dog-cat">
                                    <h1 class="font-animais4">%s</h1>
                                    <p class="font-animais">%s<br>
                                    O que acha de conseguir um novo amiguinho?</p>
                                    <h2 class="font-animais4">Características</h2>
                                    <p class="font-animais3">Gênero: %s</p>
                                    <p class="font-animais3">Porte: %s</p>
                                    <p class="font-animais3">Tipo: %s</p>
                                    <a class="btn-adote" href="/pageLogin" target="_blank">Me adote!</a>
                                    <div class="dec-pata">
                                        <img class="pata-org" src="/assets/Patinha.png" alt="">
                                        <img class="pata-org" src="/assets/Patinha.png" alt="">
                                        <img class="pata-org" src="/assets/Patinha.png" alt="">
                                    </div>
                                </div>
                            </div>
                        </section>
                ''' % (dados[0]["ani_foto"],dados[0]["ani_nome"],dados[0]["ani_tipo"],dados[0]["ani_nome"],dados[0]["ani_desc"],dados[0]["ani_sexo"],
                dados[0]["ani_porte"], dados[0]["ani_tipo"])

        return html