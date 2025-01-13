import os
from celery import Celery
from celery.schedules import crontab,schedule

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app',include=['app.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_due_date_reminder_task": {
        "task": "send_due_date_reminder_task",
        "schedule": crontab(hour=0),
    },
}