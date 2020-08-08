from rest_framework import serializers

from .models import *


class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    activity_period = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_activity_period(self, instance):
        serializer = ActivityPeriodSerializer(instance.users.all(), many=True)
        return serializer.data

