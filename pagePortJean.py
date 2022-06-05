import cherrypy


class PaginaPortJean():
    pag = open("html/PortfolioJean.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.Port()

    def Port(self):
        html = self.pag
        return html