import os
import sys
import flask
import gevent.pywsgi
from flask_executor import Executor
from platformshconfig import Config


# Coding
app = Flask(__name__)
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
    os.system("lscpu")




if __name__ == "__main__":
    http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    http_server.serve_forever()
