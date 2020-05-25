from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import ActivitiesSerializer
from .models import Activity

class ActivitiesListView(APIView):
    permissions_classes = [IsAuthenticated]
    
    def get(self, request):
        activities = request.user.activities.all()
        seriliazer = ActivitiesSerializer(activities, many=True)
        return Response(seriliazer.data)

    def post(self, request):
        request.data['user'] = request.user.pk
        serializer = ActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivitiesDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            activity = request.user.activities.all().get(id=id)
        except Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ActivitiesSerializer(activity)
        return Response(serializer.data)


    def put(self, request, id):
        try:
            activity = request.user.activities.all().get(id=id)
        except Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ActivitiesSerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            activity = request.user.activities.all().get(id=id)
        except Activity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)