import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['PYTHON_EGG_CACHE'] = '/tmp/eggcache'

from paste.deploy import loadapp

# apuntar a development.ini o a deployment.ini segons convingui
application = loadapp('config:' + os.path.dirname(os.path.abspath(__file__)) + '/development.ini')
