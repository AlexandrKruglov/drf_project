import json
from datetime import datetime, timedelta

from django_celery_beat.models import IntervalSchedule, PeriodicTask

schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)


def set_schedule(*args, **kwargs):
    PeriodicTask.objects.create(
        interval=schedule,
        name='Importing contacts',
        task='proj.tasks.import_contacts',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
