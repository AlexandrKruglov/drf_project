from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Payments, Subscription
from materials.validators import LinkValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]

class CourseSerializer(ModelSerializer):
    quantity_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, source='lessons', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_quantity_lessons(self, obj):
        return obj.lesson_set.count()


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
