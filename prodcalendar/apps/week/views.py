from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import WeekSerializer
from .models import Week

class WeekView(APIView):
    def get(self, request):
        permission_classes = [IsAuthenticated]
        
        if request.user.week != None:
            week = Week.objects.filter(id=request.user.week.id)
            serializer = WeekSerializer(week)
            return Response(serializer.data)
        else:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)