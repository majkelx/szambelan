import cherrypy


class HelloWorld(object):
    def index(self):
        ret = '<html><body><h1>Last 500 logs</h1><table style="width:100%">'
        for log in self.logs:
            ret += '<tr>'
            for fld in log.values():
                ret += '<td>' + fld + '</td>'
            ret += '</tr>'
        ret += '</table></body></html>'
        return ret
    index.exposed = True

class ClientCtr(object):
    def index(self):
        return 'Hello World! from python szmbelan ClientCtr, '
