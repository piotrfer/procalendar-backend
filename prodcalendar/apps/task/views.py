from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import TasksSerializer
from .models import Task

class TasksListView(APIView):
    permissions_classes = [IsAuthenticated]
    
    def get(self, request):
        tasks = request.user.tasks.all()
        seriliazer = TasksSerializer(tasks, many=True)
        return Response(seriliazer.data)

    def post(self, request):
        request.data['user'] = request.user.pk
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class TaskDetailView(APIView):
    permissions_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            task = request.user.tasks.all().get(id=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TasksSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            task = request.user.tasks.all().get(id=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            task = request.user.activities.all().get(id=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)