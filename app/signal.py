import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.models import User
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from app.models import Product  # Modelni Product bo'limiga moslashtiring


def send_daily_email():


        message = "Bugun bizda yangi mahsulotlar qo'shildi"


        # Barcha foydalanuvchilarga xabar yuborish

        users = User.objects.all()  # User modelini moslashtiring
        for user in users:
            send_mail(
                'Bugun bizda yangi mahsulotlar',
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )


# Har kuni 8:00 da xabarni yuborish uchun ishga tushirish
schedule.every().day.at("08:00").do(send_daily_email)

while True:
    schedule.run_pending()
    time.sleep(1)
