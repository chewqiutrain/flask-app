from logging import debug
import random
from flask import Flask
from service.service import Service
from celery import Celery 
import random
import tasks 

webapp = Flask(__name__)
# svc = Service()
# CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"

# webapp.config["CELERY_BROKER_URL"] = CELERY_BROKER_URL
# webapp.config["CELERY_RESULT_BACKEND"] = CELERY_BROKER_URL

# celery_app = Celery(webapp.name, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
# celery_app.conf.update(webapp.config)

# @celery_app.task
# def task_do_slow():
#     res = svc.do_slow()
#     return res


@webapp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@webapp.route("/ping")
def ping():
    return "pong"


@webapp.route("/db")
def do_logic():
    upid = 1
    sleep = random.choice([1,2,3])
    svc.call_database(upid, sleep)
    return f"do_logic | upid: {upid} Slept for {sleep} seconds"


@webapp.route("/do-slow")
def app_do_slow():
    res = tasks.svc_do_slow.delay()
    return "running do-slow "

if __name__ == "__main__":
    webapp.run(debug=True)