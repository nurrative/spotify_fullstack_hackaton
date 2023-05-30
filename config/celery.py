import os
from celery import Celery
from datetime import timedelta


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_new_products-every_day": {
        "task": "songs.tasks.send_new_song",
        "schedule": timedelta(minutes=1)
    }
}