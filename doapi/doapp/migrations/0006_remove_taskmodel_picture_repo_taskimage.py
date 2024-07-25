# Generated by Django 5.0.7 on 2024-07-25 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doapp', '0005_alter_taskmodel_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='picture_repo',
        ),
        migrations.CreateModel(
            name='TaskImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_repo', models.ImageField(blank=True, null=True, upload_to='task_images')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='doapp.taskmodel')),
            ],
        ),
    ]