from rest_framework import serializers
from .models import Week
from ..activity.serializers import ActivitiesSerializer

class WeekSerializer(serializers.ModelSerializer):
    activities = ActivitiesSerializer(read_only=True, many=True)
    
    class Meta:
        model = Week
        fields = [
            'id',
            'activities',
        ]
