from flask import Flask, render_template
from time import time, ctime, strftime, localtime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
app = Flask(__name__, static_folder='build',
            static_url_path='/', template_folder='build')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def get_current_time():
    t = time()
    return {'time': strftime('%c', localtime())}
    


@app.route('/content')
def content():
    return {'content': 'https://www.linkedin.com/in/faguiro/'}

""" @app.route('/api')
def content():
    return render_template('api.html') """
