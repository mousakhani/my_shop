from celery import task
from django.core.mail import send_mail
from orders.models import Order


@task
def order_created(order_id):
	"""
	Task to send an email notification when an order is successfully created.
	"""
	order = Order.objects.get(id=order_id)
	subject = f'Order {order.id}'
	message = f'Dear {order.first_name}, \n\n You have successfully placed an order.\n\n Your order id is: {order.id}'
	mail_sent = send_mail(subject, message, 'admin@myshop.com', ['khodemousa@gmail.com', ])
	return mail_sent
