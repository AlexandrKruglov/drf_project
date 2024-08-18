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


@shared_task
def deactivate_user():
    print('1!!!!!')
    users = User.objects.all()
    for user in users:
        if user.last_login.date() < (timezone.now() - timedelta(days=30)):
            user.is_active = False
            print(f'{user} отключен')
            user.save()
