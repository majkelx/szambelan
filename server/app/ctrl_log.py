import cherrypy

class LogService(object):
    exposed = True


    @cherrypy.tools.accept()
#     def GET(self):
#         return cherrypy.session['mystring']

    @cherrypy.tools.json_in()
    def POST(self):
        log =  cherrypy.request.json
        print (log)

#     def PUT(self, another_string):
#         cherrypy.session['mystring'] = another_string

#     def DELETE(self):
#         cherrypy.session.pop('mystring', None)
