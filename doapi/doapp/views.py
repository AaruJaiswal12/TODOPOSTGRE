from django.shortcuts import render
from .models import TaskModel
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer
from rest_framework import status

class TaskView(APIView):

    def get(self,request,format=None):
        ob=TaskModel.objects.all()
        serializer=TaskSerializer(ob,many=True)
     
        return Response({"msg":"Data is fetched","data":serializer.data},status=status.HTTP_200_OK)

        

    def post(self,request,format=None):
        serializer=TaskSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data is created","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors) 
        
    def put(self,request,format=None):
        ob=TaskModel.objects.get(user_id=request.data["user_id"])  
        serializer=TaskSerializer(ob,request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response({"msg":"Data is updated successfully"},serializer.data)
        return Response(serializer.errors)
    

    def delete(self,request,format=None):
        ob=TaskModel.objects.get(user_id=request.data["user_id"])
        ob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

        




# Create your views here.


"""
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskModel
from .serializers import TaskSerializer

class TaskView(APIView):

    def get(self, request, format=None):
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        instance = get_object_or_404(TaskModel, user_id=request.data.get('user_id'))
        serializer = TaskSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        instance = get_object_or_404(TaskModel, user_id=request.data.get('user_id'))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""

