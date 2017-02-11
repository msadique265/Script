from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('distributor',
             broker='amqp://', #localhost
			 # broker='amqp://<user>:<password>@<ip>/<vhost>'), #for remote host
             backend='amqp://',
             include=['distributor.tasks'])

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()