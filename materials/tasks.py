from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django_celery_beat.models import IntervalSchedule

from config import settings
from materials.models import Subscription
from users.models import User


@shared_task
def send_information_about_update_course(course):
    update_course = Subscription.objects.filter(course=course)
    for item in update_course:
        send_mail(
            subject='обноыление курса',
            message='курс был обновлен.ознакмтесь с обновлением',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[item.user.email],
            fail_silently=False,
        )


@shared_task(name='materials.tasks.deactivate_user')
def deactivate_user():
    users = User.objects.filter(is_active=True, is_superuser=False,  last_login__isnull=False)
    print(users)
    if users.exists():
        for user in users:
            print(user.last_login)
            if user.last_login < (timezone.now() - timedelta(days=30)):
                user.is_active = False
                print(f'{user} отключен')
                user.save()
