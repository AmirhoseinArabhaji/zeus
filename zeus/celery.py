import os

from celery import Celery
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zeus.settings')

celery_app = Celery('zeus')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.conf.task_default_queue = 'default'
celery_app.autodiscover_tasks()

celery_app.conf.task_queues = (
    Queue('default', queue_arguments={'x-max-priority': 5}),
    Queue('high_priority', queue_arguments={'x-max-priority': 10}),
    Queue('low_priority', queue_arguments={'x-max-priority': 3}),
)

celery_app.conf.beat_schedule = {

}

"""
HELP: Running Celery Command 

celery -A zeus worker -B  -l info

or

celery -A zeus worker -B  -l info -Q  default,high_priority,low_priority

or 

FOR RUNNING ON WINDOWS:

Celery 4.0+ does not officially support window already. 

celery -A zeus worker -B -l info -Q  default,high_priority,low_priority --pool=solo


On Production:

celery -A zeus worker -l debug --logfile=/usr/src/app/celery.log -Q default,high_priority,low_priority --detach

"""
