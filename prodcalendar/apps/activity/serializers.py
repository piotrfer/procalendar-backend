from rest_framework import serializers
from .models import Activity

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'