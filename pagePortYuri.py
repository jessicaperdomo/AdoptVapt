import cherrypy


class PaginaPortYuri():
    pag = open("html/PortfolioYuri.html", encoding='UTF8').read()

    @cherrypy.expose()
    def index(self):
        return self.Port()

    def Port(self):
        html = self.pag
        return html