import cherrypy

class PaginaSobre():
    sobreP = open("html/sobreP.html", encoding='UTF8').read()
    nav = open("html/navbar.html", encoding='UTF8').read()
    rodape = open("html/rodape.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.SobrePortfolios()

    def SobrePortfolios(self):
        html = self.nav
        html = html + self.sobreP
        html = html + self.rodape

        return html