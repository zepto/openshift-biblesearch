
#
import imp
import os

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#


def run_simple_httpd_server(app, ip, port=8080):
   from wsgiref.simple_server import make_server
   make_server(ip, port, app).serve_forever()

#
#  main():
#
if __name__ == '__main__':
    ip   = 'localhost'
    port = 8081
    app = imp.load_source('application.bible_app', 'wsgi/application')
    print('Starting WSGIServer on %s:%d ... ' % (ip, port))
    run_simple_httpd_server(app.bible_app, ip, port)
    #
    #
    # from bottle import run
    # run(app.app, host=ip, port=port, reloader=True)
