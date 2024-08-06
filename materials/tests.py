from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class TestLessons(APITestCase):
    """ Тестирование уроков """

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@mail.ru")
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name="Test", description="Test")
        self.lesson = Lesson.objects.create(
            course=self.course,
            name="Test_lesson",
            description="Test_lesson",
            owner=self.user,
            link="https://www.youtube.com",
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """

        url = reverse("materials:lessons_create")
        data = {
            "name": "Test_lesson",
            "description": "Test_lesson",
            "course": self.lesson.course.id,
            "link": "https://www.youtube.com",
        }

        response = self.client.post(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)
        self.assertEqual(data.get("name"), "Test_lesson")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("link"), "https://www.youtube.com")
        self.assertEqual(data.get("description"), "Test_lesson")

    def test_update_lesson(self):
        """ Тестирование изменений урока """

        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Test_lesson",
            "description": "Test_lesson",
            "course": self.lesson.course.id,
            "link": "https://www.youtube.com",
        }
        response = self.client.put(url, data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("description"), "Test_lesson")
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)


    def test_retrieve_lesson(self):
        """ Тестирование просмотра одного урока """

        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("description"), self.lesson.description)
        self.assertEqual(data.get("course"), self.lesson.course.id)
        self.assertEqual(data.get("owner"), self.lesson.owner.id)

    def test_delete_lesson(self):
        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        print(response)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCreate(APITestCase):
    """ Тестирование подписок """

    def setUp(self):
        self.user = User.objects.create(email="admin@lmail")
        self.course = Course.objects.create(name="Test", description="Test")
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        """Тестирование активации подписки"""

        self.url = reverse("materials:subscriptions-create")
        data = {"user": self.user.id, "course": self.course.id}
        response = self.client.post(self.url, data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(
            Subscription.objects.filter(user=self.user, course=self.course).exists(),
            True,
        )
        self.assertEqual(response.json().get("message"), "подписка добавлена")


class SubscriptionTestDelete(APITestCase):
    """ Тестирование подписок """


def setUp(self):
    self.user = User.objects.create(email="admin@lmail")
    self.course = Course.objects.create(name="Test", description="Test")
    self.client.force_authenticate(user=self.user)
    self.subscriptions = Subscription.objects.create(user=self.user, course=self.course)


def test_subscription_delete(self):
    self.subscriptions = Subscription.objects.create(user=self.user, course=self.course)
    url = reverse("users:subscriptions-delete", args=(self.subscriptions.pk,))
    response = self.client.delete(url)

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Lesson.objects.all().count(), 0)
