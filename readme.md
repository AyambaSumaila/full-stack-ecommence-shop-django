# Shopping cart - using django.sessions.models

## Using Django with Celery and RabbitMQ

## Celery is a distributed task queue that can process vast amounts of messages

docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.31.1-management

Running a Celery worker
A Celery worker is a process that handles bookkeeping features like sending/receiving queue messages,
registering tasks, killing hung tasks, tracking status, and so on. A worker instance can consume from
any number of message queues.
Open another shell and start a Celery worker from your project directory, using the following command:
celery -A myshop worker -l info



Monitoring Celery with Flower
Besides the RabbitMQ management UI, you can use other tools to monitor the asynchronous tasks
that are executed with Celery. Flower is a useful web-based tool for monitoring Celery. You can find
the documentation for Flower at https://flower.readthedocs.io/.
Install Flower using the following command:
python -m pip install flower==2.0.1


Flower should never be deployed openly in a production environment without security. Let’s add au-
thentication to the Flower instance. Stop Flower using Ctrl + C, and restart it with the --basic-auth
option by executing the following command:
celery -A myshop flower --basic-auth=user:pwd

"""
Summary
In this chapter, you created a basic e-commerce application. You made a product catalog and built a
shopping cart using sessions. You implemented a custom context processor to make the cart available to
all templates and created a form for placing orders. You also learned how to implement asynchronous
tasks using Celery and RabbitMQ. Having completed this chapter, you now understand the foundational
elements of building an e-commerce platform with Django, including managing products, process-
ing orders, and handling asynchronous tasks. You are now also capable of developing projects that
efficiently process user transactions and scale to handle complex background operations seamlessly.
In the next chapter, you will discover how to integrate a payment gateway into your shop, add custom
actions to the administration site, export data in CSV format, and generate PDF files dynamically.

"""

""" Stripe Account creation process """
We will continue by installing the Stripe Python SDK and adding Stripe to our Django project.
Installing the Stripe Python library
Stripe provides a Python library that simplifies dealing with its API. We are going to integrate the
payment gateway into the project using the stripe library.
You can find the source code for the Stripe Python library at https://github.com/stripe/stripe-
python.
Install the stripe library from the shell using the following command:
python -m pip install stripe==9.3.0

Stripe account ID "acct_1Q79YxJUhWAw5UW2"