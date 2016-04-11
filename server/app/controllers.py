import cherrypy


class HelloWorld(object):
    def index(self):
        return 'Hello World!  from python szmbelan HelloWorld controller'
    index.exposed = True

class ClientCtr(object):
    def index(self):
        return 'Hello World! from python szmbelan ClientCtr, '
