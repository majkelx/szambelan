import cherrypy


class HelloWorld(object):
    def index(self):
        ret = '<html><body><table style="width:100%">'
        for log in self.logs:
            ret += '<tr><td>' + log['ts'] + '</td><td>' + log['fid'] + '</td><td>' + log['raw'] + '</td></tr>'
        ret += '</table></body></html>'
        return ret
    index.exposed = True

class ClientCtr(object):
    def index(self):
        return 'Hello World! from python szmbelan ClientCtr, '
