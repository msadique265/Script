from __future__ import absolute_import, unicode_literals
from .celery import app
from celery.utils.log import get_task_logger
from celery.backends.amqp import AMQPBackend
import time


log = get_task_logger(__name__)

@app.task(backend=AMQPBackend(app, url='amqp://'))
def add(x,y):
	log.info('Calling task add(%d, %d)'%(x,y))
	print('I am in task add')
	z = sum(x,y)
	return z

def sum(x, y):
	time.sleep(10)
	return(x+y)
