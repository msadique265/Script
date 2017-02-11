# Distributed processing using celery in python

On distributor/broker machine:

A) Install Celery & RabbitMQ.

B) Configure RabbitMQ so that another Machine can connect to it.

configuration:
- add new user = 
rabbitmqctl add_user <user> <password>

- add new virtual host = 
rabbitmqctl add_vhost <vhost_name>

- set permissions for user on vhost = 
rabbitmqctl set_permissions -p <vhost_name> <user> ".*" ".*" ".*"

- restart rabbit = 
rabbitmqctl restart

- Note: you can find rabbitmqctl on windows at C:\Program Files\RabbitMQ Server\rabbitmq_server-3.6.6\sbin

On worker machine:

A) Add worker details in celery.py

B) Start worker from project directory (celery -A distributor worker -l info)

- Note: you can run multiple worker on same machine

worker1(cmd) : celery -A distributor worker -l info -n worker1%n

worker2(cmd) : celery -A distributor worker -l info -n worker2%n

That's it.

You can test it using client.py

Thank you!

Md Sadique
