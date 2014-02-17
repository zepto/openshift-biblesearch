#!/usr/bin/env python

#
# This file may be used instead of Apache mod_wsgi to run your python
# web application in a different framework.  A few examples are
# provided (cherrypi, gevent), but this file may be altered to run
# whatever framework is desired - or a completely customized service.
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
    ip   = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    app = imp.load_source('application.bible_app', 'wsgi/application')
    print('Starting WSGIServer on %s:%d ... ' % (ip, port))
    run_simple_httpd_server(app.bible_app, ip, port)

    # from bottle import run
    # run(app.app, host=ip, port=port, reloader=True)
