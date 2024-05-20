from flask import render_template
from flask import Flask
from threading import Thread

app = Flask('')

@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html', title='test-bot')

def run():
    app.run(host='0.0.0.0', port=3000)

def keep_alive():
    t = Thread(target=run)
    t.start()
