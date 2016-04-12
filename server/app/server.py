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
    logsvc = LogService()
    hello = HelloWorld()
    hello.logs = logsvc.logs
    cherrypy.tree.mount(hello, '/',    config=get_app_config())
    cherrypy.tree.mount(logsvc, '/log', config=get_logsvc_config())
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    start()