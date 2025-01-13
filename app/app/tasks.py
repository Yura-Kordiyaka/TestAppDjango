from app.celery_app import app
from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from tasks.models import Task
from django.utils import timezone
from django.conf import settings

@shared_task
def send_task_assignment_notification(assignee_email, task_name):
    subject = 'New Task Assigned'
    message = f'You have been assigned a new task: {task_name}.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [assignee_email])


@shared_task
def send_task_update_notification(assignee_email, task_name):
    subject = 'Task Updated'
    message = f'The task "{task_name}" has been updated.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [assignee_email])


@app.task(name='send_due_date_reminder_task')
def send_due_date_reminder_task():
    now = timezone.now()
    upcoming_due_date = now + timedelta(days=1)

    tasks_due_soon = Task.objects.filter(
        due_date__lte=upcoming_due_date,
        due_date__gt=now,
        reminder_sent=False,
        assigned__isnull=False,
    ).select_related('assignee')

    for task in tasks_due_soon:
        if task.assignee and task.assignee.email:
            subject = 'Task Due Date Reminder'
            message = f'The due date for the task "{task.title}" is approaching on {task.due_date}.'
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [task.assignee.email]
            )
            task.reminder_sent = True
            task.save()
