from django.db import models

# Create your models here.

class TaskModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    due_date=models.DateTimeField(auto_now_add=True)



class TaskImage(models.Model):
    task = models.ForeignKey(TaskModel, related_name='images', on_delete=models.CASCADE)
    images = models.FileField(blank=True,null=True,upload_to="task_images")

    def __str__(self):
        return f"Image for Task {self.task.title}"