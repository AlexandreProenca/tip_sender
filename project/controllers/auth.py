# -*- coding: utf-8 -*-
from project import app
from bottle import template, request, redirect, response
from datetime import datetime
from firebase import firebase
from push_thread import PushThread


@app.route('/', method='GET')
def index():
    return template('index', message='')


@app.route('/login', method=['POST'])
def login():
    username = request.POST['username']
    password = request.POST['password']

    if username == 'admin' and password == 'f':
        response.set_cookie("account", username, secret='!2jasdk332*hjsdhjjj', max_age=18000)
        return redirect('/panel', code=302)

    else:
        return template('index', message='Username or password invalid')


@app.route('/login', method=['GET'])
def login():
    return template('index', message='')


@app.route('/panel', method=['GET'])
def panel():
    username = request.get_cookie("account", secret='!2jasdk332*hjsdhjjj')
    if username:
        return template("panel", message='')
    else:
        return template("index", message="You are not logged in. Access denied.")


@app.route('/panel', method=['POST'])
def panel():
    try:
        firebase.FirebaseApplication("https://app4tips.firebaseio.com", None).post('/analises', {
            "nome": request.POST['nome'],
            "tip": request.POST['tip'],
            "hora": server_time()
        })
    except Exception as e:
        print "EXceptipn ", e

    p = PushThread(request.POST['nome'], request.POST['tip'], server_time())
    p.start()

    return template('panel', message='Your tip was sent success!')


def server_time():
        today = datetime.now()
        return str(today.hour) + ':' + str(today.minute)