#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import socket
import json

url = "YOUR VIWER STATS LINK"
webhook_url = "DISCORD WEBHOOK LINK"
ip = socket.gethostbyname(socket.gethostname())
pc = socket.gethostname()

def spam():
    for i in range(4000):  # Times that we want to spam link
        # print(f'[+] Link Spammed {i + 1} time/s.')
            requests.get(url)
            time.sleep(2)
    main_content = {
        "username": "GitHub Viwer Spam",
        "avatar_url": "",
        "content": "",

        "embeds": [
            {
                "title": "NEW ATTACK",
                "description": f"New Bot Attack from **{pc}**, (`{ip}`)",
                "color": 0xff0000,
            },
            {
                "title": "NEW ATTACK",
                "description": f"Spammed Link: [Click Here]({url}) | {i+1} time/s",
                "color": 0x00ffff,
            }
        ]
    }
    requests.post(webhook_url, json.dumps(main_content), headers={'Content-Type': 'application/json'})

spam()