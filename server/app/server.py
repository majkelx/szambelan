import cherrypy
import os

## config import

from controllers import HelloWorld
from ctrl_log import LogService

HERE = os.path.dirname(os.path.abspath(__file__))


def get_app_config():
    return {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(HERE, 'static'),
        }
    }

def get_logsvc_config():
    return {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.json_in.force': True,
        }
    }


def start():
    print (HERE)
    cherrypy.tree.mount(HelloWorld(), '/',    config=get_app_config())
    cherrypy.tree.mount(LogService(), '/log', config=get_logsvc_config())
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    start()