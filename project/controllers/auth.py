# -*- coding: utf-8 -*-
from project import app
from bottle import template, request
from datetime import datetime
from firebase import firebase


FIREBASE_URL = "https://app4tips.firebaseio.com"

debug = True

@app.route('/', method='GET')
def index():
    return template('index', message='')


@app.route('/', method=['POST'])
def login():
    try:
        firebase.FirebaseApplication(FIREBASE_URL, None).post('/analises', {
            "nome": request.POST['nome'],
            "hora": request.POST['tip'],
            "tip": server_time()
        })

    except Exception as e:
        print "EXceptipn ", e

    return template('index', message='')


def server_time():
        today = datetime.now()
        return str(today.hour) + ':' + str(today.minute)