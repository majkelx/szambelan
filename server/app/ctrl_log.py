import cherrypy

class LogService(object):
    exposed = True

    logs = []

    @cherrypy.tools.accept()
#     def GET(self):
#         return cherrypy.session['mystring']

    @cherrypy.tools.json_in()
    def POST(self):
        log =  cherrypy.request.json
        for frame in log['frames']:
            frame['ver'] = log['ver']
            frame['dev'] = log['dev']
            self.logs.insert(0, frame)
            if len(self.logs) > 500:
                self.logs.pop()
        print (log)

#     def PUT(self, another_string):
#         cherrypy.session['mystring'] = another_string

#     def DELETE(self):
#         cherrypy.session.pop('mystring', None)
