import time

from celery import shared_task
@shared_task(max_retries=5)
def some_task():
    time.sleep(5)
    return 'hello'


@shared_task
def some_scheduled_task():
    return 'Darova'