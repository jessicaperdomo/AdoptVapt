import cherrypy
from classes.Animais import *

class PaginaAnimais():
    nav = open("html/navbar.html", encoding='UTF8').read()
    rodape = open("html/rodape.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.AnimalP()

    def AnimalP(self):
        html = self.nav

        html = html + '''
           <section class="animais-disp">
        '''

        html += self.CriaAnimal()

        html = html + self.rodape
        return html

    def CriaAnimal(self):
        html = '''
            <h1 class="titulo-animais-disponiveis">Animais Disponíveis</h1>
        '''
        objAni = Animais()
        dados = objAni.obterTodosAnimais()

        aux = 1
        for ani in dados:
            if aux == 2:
                html += '''
                    <div class="coluna1">
                '''

            html += '''
                    <div class="item-animais-disp">
                        <a href="/pageAnis" target="_blank"><img class="foto-animal" src="/assets/%s"
                        alt="%s"></a>
                        <h2 class="font-animais2">%s</h2>
                        <p class="font-animais">%s</p>
                        <a class="btn-adote" href="/pageAnis/conhecaAni?pId=%s" target="_blank">Me conheça!</a>
                    </div>
            ''' % (ani["ani_foto"],ani["ani_tipo"],ani["ani_nome"],ani["ani_sexo"],ani["ani_id"])

            if aux == 2:
                html += '''
                    </div>
                '''
                aux=0

            aux = aux + 1

        html += '''
            </section>
        '''
        return html