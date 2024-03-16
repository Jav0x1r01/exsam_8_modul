# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from app.models import User
from datetime import datetime
from .models import Product

@shared_task
def send_new_product_notification():
    users = User.objects.all()
    new_products = Product.objects.filter(created_at__date=datetime.now().date())
    subject = 'Yangi mahsulotlar'
    message = 'Bugun bizga quyidagi mahsulotlar qo\'shildi:\n'
    for product in new_products:
        message += f'- {product.name}\n'
    for user in users:
        send_mail(subject, message, 'from@example.com', [user.email])
