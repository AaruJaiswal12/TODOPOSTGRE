# Generated by Django 5.0.7 on 2024-07-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doapp', '0008_alter_taskimage_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskimage',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='task_images'),
        ),
    ]