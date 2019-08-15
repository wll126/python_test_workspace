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

app=Flask(__name__) #创建一个wsgi应用


@app.route('/')   # 添加路由 ：根
def test_first():
    print("测试首先接口")
    return "返回一个字符串 hello"


@app.route('/login', methods=['GET','POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    print("user:%s,password:%s" %(username,password))
    return 'post request'

@app.route("/set_cookie")
def set_cookie():
    print("测试设置cookie")
    response=make_response('<h1>This web carries a cookie!</h1>')
    # 设置cookie有效时间
    outdate=datetime.datetime.today()+datetime.timedelta(days=30)
    response.set_cookie('username','evancss',expires=outdate)
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


if __name__ =="__main__":
    app.run(debug=True)

