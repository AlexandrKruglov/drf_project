from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Payments, Subscription
from materials.validators import LinkValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer(read_only=True, source='lessons_set', many=True)
    subscription = SubscriptionSerializer(read_only=True)
    quantity_lessons = serializers.SerializerMethodField()

    # subscription_inf = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_quantity_lessons(self, obj):
        return obj.lesson_set.count()

    def get_subscription(self, course):
        user = self.context.get('request').user
        course = self.context.get('view').kwargs.get('pk')
        subscription = Subscription.objects.filter(user=user, course=course)
        if subscription.exists():
            return True
        else:
            return False


class CourseDitailSerializer(serializers.ModelSerializer):
    quantity_lessons = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(read_only=True, many=True, source='lessons_set')
    subscription = serializers.SerializerMethodField(read_only=True)

    def get_quantity_lessons(self, obj):
        return obj.lesson_set.count()

    def get_subscription(self, course):
        user = self.context.get('request').user
        course = self.context.get('view').kwargs.get('pk')
        subscription = Subscription.objects.filter(user=user, course=course)
        if subscription.exists():
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'quantity_lessons', 'lesson', 'subscription']


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
