# Started from code at https://github.com/potatolondon/djappengine/blob/master/main.py

import os
import sys
import logging
# main.py appears to get called multiple times and so if we just extend sys.path
# like below many copies of the paths will be continuously appended to sys.path.
#sys.path.extend(['portfolio_project', 'lib', 'vlib'])
if 'portfolio_project' not in sys.path:
    sys.path.extend(['portfolio_project', 'lib', 'vlib'])
# below crashed server
#from werkzeug.debug import DebuggedApplication

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

os.environ['APPENGINE_PRODUCTION'] =\
    os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or\
    os.getenv('SETTINGS_MODE') == 'prod'

import django
import django.core.signals
import django.dispatch

if not os.getenv('APPENGINE_PRODUCTION'):
    logging.info('Development django: %s' % django.__file__)
    logging.info(django.get_version())


# Log exceptions
def log_exception(*args, **kwds):
    logging.exception('Exception in request:')

django.dispatch.Signal.connect(
    django.core.signals.got_request_exception, log_exception)


# WSGI app
from django.core.handlers.wsgi import WSGIHandler
app = WSGIHandler()
#app = DebuggedApplication(app, evalex=True)