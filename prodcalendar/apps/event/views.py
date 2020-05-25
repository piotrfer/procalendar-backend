from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import EventsSerializer

class EventsListView(APIView):
    permissions_classes = [IsAuthenticated]
    
    def get(self, request):
        events = request.user.events.all()
        seriliazer = EventsSerializer(events, many=True)
        return Response(seriliazer.data)