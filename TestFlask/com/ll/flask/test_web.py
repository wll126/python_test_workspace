# !/usr/bin/python
# coding=utf8

"""
测试flask 框架使用，创建web项目
"""
from flask import Flask
from flask import make_response
import datetime
from flask import request
from flask import redirect
from flask import abort
from flask import render_template

app=Flask(__name__,template_folder="templates",static_folder='static') # 创建一个wsgi应用


@app.route('/')   # 添加路由 ：根
def test_first():
    print("测试首先接口")
    req=request
    response=make_response()
    response.set_cookie('index','2')
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    print("user:%s,password:%s" %(username,password))
    return 'post request login successful!'

@app.route("/set_cookie")
def set_cookie():
    print("测试设置cookie")
    response=make_response('<h1>This web carries a cookie!</h1>')
    # 设置cookie有效时间
    outdate=datetime.datetime.today()+datetime.timedelta(days=30)
    response.set_cookie('username','evancss',expires=outdate)
    response.set_cookie('password', '123456', expires=outdate)
    response.set_cookie('logintime', str(datetime.datetime.today()), expires=outdate)
    return response

@app.route('/get_cookie')
def get_cookie():
    print("获取cookie")
    name=request.cookies.get('username')
    return name

@app.route('/del_cookie')
def del_cookie():
    print("删除cookie")
    response=make_response('delete_cookie')
    response.set_cookie('username','',expires=0)
    response.delete_cookie('username')
    return response

@app.route('/redir')
def redir():
    print("重定向")
    return redirect('get_cookie')


@app.route('/user/<id>')
def test_abort(id):
    print("测试abort")
    if int(id)>10:
        abort(404)
    return '<h1>hello ,%s </h1>' % id

@app.route('/get_info')
def test_get_request_infos():
    print("测试请求信息")
    args=request.args
    form=request.form
    headers=request.headers
    url=request.url
    origin=request.cookies
    print('args=',args)
    print('form=',form)
    print('headers=',headers)
    print('url=',url)
    print('origin=',origin)
    return args

@app.route('/ajax/')
def test_ajax():
    # 测试ajax请求
    url=request.url
    args=request.args
    print(url,args)
    print("ajax 请求信息")
    return {"msg":"ajax 请求成功!"}


class MiddleWare:
    def __init__(self,wsgi_app):
        self.wsgi_app=wsgi_app

    def __call__(self, *args, **kwargs):
        return self.wsgi_app(*args,**kwargs)


if __name__ =="__main__":
    app.wsgi_app=MiddleWare(app.wsgi_app)
    app.run(port=9999,debug=True)

