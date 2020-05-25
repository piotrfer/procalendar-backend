from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import ActivitiesSerializer

class ActivitiesListView(APIView):
    permissions_classes = [IsAuthenticated]
    
    def get(self, request):
        activities = request.user.activities.all()
        seriliazer = ActivitiesSerializer(activities, many=True)
        return Response(seriliazer.data)
