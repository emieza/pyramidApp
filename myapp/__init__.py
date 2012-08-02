# -*- coding: utf-8 -*-

from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
   return Response('xxHello %(name)s!' % request.matchdict)
   
def main(global_config, **global_settings):
   config = Configurator()
   config.add_route('hello', '/hello/{name}')
   config.add_view(hello_world, route_name='hello')
   app = config.make_wsgi_app()
   #serve(app, host='0.0.0.0')
   return app
   
if __name__ == '__main__':
	main(False)
	
# per visualitzar l'aplicacio apunta el navegador al port indicat
# per la configuracio del .ini o del Apache (tipicament 8080 o 6543)
# http://localhost:8080/hello/qualsevolcosa
