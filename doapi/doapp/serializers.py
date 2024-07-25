from django.db import models
from rest_framework import serializers
from .models import TaskModel, TaskImage

class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    images = TaskImageSerializer(many=True)

    class Meta:
        model = TaskModel
        fields = ['username', 'title', 'description', 'completed', 'due_date', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        task = TaskModel.objects.create(**validated_data)
        
        for image_data in images_data:
            TaskImage.objects.create(task=task, **image_data)

        return task
