from flask import Flask
from time import time, ctime, strftime, localtime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
app = Flask(__name__, static_folder='../build', static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    t = time()
    return {'time': strftime('%c', localtime())}
    return {'time': ctime(t)}


@app.route('/api/content')
def content():
    return {'content': 'https://www.linkedin.com/in/faguiro/'}
