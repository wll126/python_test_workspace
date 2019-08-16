# coding:utf8

import asyncio
import threading
from aiohttp import web

"""
asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
"""


@asyncio.coroutine
def hello():
    print("Hello China (%s)" % threading.current_thread())
    # 异步调用
    yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.current_thread())

async def wget(host):
    print("wget ..%s" % host)
    connect=asyncio.open_connection(host,80)
    reader,writer=await connect
    header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line= await reader.readline()
        if line==b'\r\n':
            break
        print("%s header >%s" %(host,line.decode('utf-8').rstrip()))
    writer.close()

def test1():
    # 获取Eventloop
    loop=asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(hello())
    loop.close()

def test2():
    loop=asyncio.get_event_loop()
    tasks=[hello(),hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def test3():
    loop=asyncio.get_event_loop()
    tasks=[wget(host) for host in ['www.sina.com','www.sohu.com','www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body='<h1>index</h1>')

async def hello2(request):
    await asyncio.sleep(0.5)
    text='<h1>Hello %s</h1>' % request.match_info['name']
    return web.Response(body=text)

async def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello2)
    srv=await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print("Server started at http://127.0.0.1:8000...")
    return srv

def test5():
    loop=asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()


if __name__=="__main__":
    test5()
    print("go on")
