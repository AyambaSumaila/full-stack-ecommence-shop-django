from celery import shared_task 

from django.core.mail import send_mail
from .models import Order 


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order #{order_id} has been created'
    message = f'Dear {order.first_name},\n\nYour order has been successfully placed. You can track it here: http://example.com/orders/{order_id}\n\nBest regards,\nYour Shop'

    
    mail_sent=send_mail(subject, message, 'admin@gmail.com', [order.email])
    return f'Email sent: {mail_sent}'

    