from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import TasksSerializer

class TasksListView(APIView):
    permissions_classes = [IsAuthenticated]
    
    def get(self, request):
        tasks = request.user.tasks.all()
        seriliazer = TasksSerializer(tasks, many=True)
        return Response(seriliazer.data)
