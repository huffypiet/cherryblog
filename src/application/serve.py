###
#
#   Version: 1.0.0
#   Date: 2020-03-29
#   Author: Yves Vindevogel (vindevoy)
#
###

import cherrypy

from dataloader import DataLoader
from settings import Settings
from singleton import Singleton
from templateloader import TemplateLoader


class Application(metaclass=Singleton):
    @cherrypy.expose
    def index(self):
        template = TemplateLoader('src/theme/default').get_template('index.html')
        rendered = template.render(data=DataLoader().get_data())

        return rendered


if __name__ == '__main__':
    cherrypy.quickstart(Application(), config=Settings().server_config)