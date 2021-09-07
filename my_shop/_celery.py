import os

# set the default django settings module for the celery program
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')

app = Celery('myshop')
# namespace
# زمانی که در فایل settings می خواهیم تنظیمات سلری را انجام دهیم، پیشوند تنظیمات خواهد بود
# مثلا:
# CELERY_BROKER_URL
app.config_from_object('django.conf:settings', namespace='CELERY')
# متد زیر فایل هایی به نام tasks.py را در همه ی اپ های معرفی شده به جنگو را می گردد
# و هر کدام تسکی داشته باشند به سلری اضافه می کند
app.autodiscover_tasks()

