from spyne import Application,rpc,ServiceBase,Iterable,Integer,Unicode
from spyne.protocol.soap import Soap11,Soap12
from spyne.server.wsgi import WsgiApplication


class HelloService1(ServiceBase):
    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
    def say_hello1(ctx,name,times):
        for i in range(times):
            yield "say_hello1 : Hello,%s" % name

    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
    def say_hello2(ctx,name,times):
        for i in range(times):
            yield "say_hello2: Hello, %s" % name


class HelloService2(ServiceBase):
    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
    def say_hello3(ctx,name,times):
        for i in range(times):
            yield "say_hello1 : Hello,%s" % name

    @rpc(Unicode,Integer,_returns=Iterable(Unicode))
    def say_hello4(ctx,name,times):
        for i in range(times):
            yield "say_hello2: Hello, %s" % name


application=Application([HelloService1,HelloService2],'http://schemas.xmlsoap.org/soap/envelop',in_protocol=Soap11(validator='lxml'),out_protocol=Soap11())
wsgi_application=WsgiApplication(application)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import  make_server
    logging.basicConfig(level=logging.DEBUG)
    # 10.106.72.6
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    logging.info("listening to Http://10.106.72.6:8000")
    logging.info("wsdl is at: http://10.106.72.6:8000/?wsdl")
    server=make_server("10.106.72.6",8000,wsgi_application)
    server.serve_forever()


