# -*- coding: utf-8 -*-
from project import app
from bottle import template, request, redirect, response
from datetime import datetime
from firebase import firebase
import time
from push_thread import PushThread


@app.route('/', method='GET')
def index():
    return template('index', message='')


@app.route('/login', method=['POST'])
def login():
    username = request.POST['username']
    password = request.POST['password']

    if username == 'admin' and password == 'f':
        response.set_cookie("account", username, secret='!2jasdk332*hjsdhjjj')
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
    tempo = time.time()
    try:
        firebase.FirebaseApplication("https://moneyalert.firebaseio.com", None).post('/live_tips', {
            "created": tempo,
            "tip": request.POST['tip'],
            "image_src": "img/bola.png",
            "title": request.POST['title'],
        })
    except Exception as e:
        print "EXceptipn ", e

    p = PushThread(request.POST['title'], request.POST['tip'], tempo)
    p.start()

    return template('panel', message='Your tip was sent success!')


def server_time():
        today = datetime.now()
        return str(today.hour) + ':' + str(today.minute)
