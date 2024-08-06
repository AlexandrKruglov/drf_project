from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import (CourseViewSet, LessonCreateAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonDestroyAPIView, LessonUpdateAPIView, PaymentsListAPIView,
                             PaymentsCreateAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView)
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_retrieve'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path("subscriptions/create/", SubscriptionCreateAPIView.as_view(), name="subscriptions-create"),
    path("subscriptions/<int:pk>/delete/", SubscriptionDestroyAPIView.as_view(), name="subscriptions-delete")
]
urlpatterns += router.urls
