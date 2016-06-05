#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import json
import threading
import requests

PUSH_PAYLOAD = {
    "app_id": "256ec056-6f96-4b61-93e3-2a3d52b37c55",
    "included_segments": ["All"],
    "ios_sound": "default",
    "priority": 10,
    "android_group": "smarttrade",
    'android_visibility': 0,
    "content_available": 1
}

PUSH_SUPPORT = False

HEADERS = {
    "Authorization": "Basic MzJiMWNhYTktYmViNi00NWJiLTk5YzctNWE3NjhmNjA3NGM4",
    "Content-Type": "application/json"
}

PUSH_URL = 'https://onesignal.com/api/v1/notifications'


class PushThread(threading.Thread):

    def __init__(self, nome, tip, hora):
        threading.Thread.__init__(self)
        self.nome = nome
        self.tip = tip
        self.hora = hora

    def run(self):
        check_and_push(self.nome, self.tip, self.hora)


def check_and_push(nome, tip, hora):
    PUSH_PAYLOAD['contents'] = {"en": "Jogo " + nome}
    r = requests.post(PUSH_URL, data=json.dumps(PUSH_PAYLOAD), headers=HEADERS)



