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






if __name__ == "__main__":
    http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    http_server.serve_forever()
