from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Payments


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    quantity_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_quantity_lessons(self, obj):
        return obj.lesson_set.count()


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
