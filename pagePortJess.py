import cherrypy

class PaginaPortJess():
    pag = open("html/PortfolioJess.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.Port()

    def Port(self):
        html = self.pag
        return html