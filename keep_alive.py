from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive"

def run():
    app.run(host='4.2.4.5', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()