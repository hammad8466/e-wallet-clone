# Generated by Django 5.0.2 on 2024-03-15 09:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0014_customuser_new_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
