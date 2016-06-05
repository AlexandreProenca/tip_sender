# -*- coding: utf-8 -*-
from project import app
from bottle import template, request
from datetime import datetime
from firebase import firebase
from push_thread import PushThread

FIREBASE_URL = "https://app4tips.firebaseio.com"


@app.route('/', method='GET')
def index():
    return template('index', message='')


@app.route('/', method=['POST'])
def login():
    try:
        firebase.FirebaseApplication(FIREBASE_URL, None).post('/analises', {
            "nome": request.POST['nome'],
            "tip": request.POST['tip'],
            "hora": server_time()
        })
    except Exception as e:
        print "EXceptipn ", e

    p = PushThread(request.POST['nome'],request.POST['tip'],request.POST['nome'])
    p.start()

    return template('index', message='')


def server_time():
        today = datetime.now()
        return str(today.hour) + ':' + str(today.minute)