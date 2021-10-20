from celery import Celery 
from service.service import Service

celery_app = Celery("tasks", broker="redis://localhost:6379", backend="redis://localhost:6379")
svc = Service()

@celery_app.task
def add(x, y):
    return x + y

@celery_app.task 
def svc_call_database(upid, sleep):
    res = svc.call_database(upid, sleep)
    return res 

@celery_app.task
def svc_do_quick():
    res = svc.do_quick()
    return res 

@celery_app.task
def svc_do_slow():
    res = svc.do_slow()
    return res 