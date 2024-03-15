# Generated by Django 5.0.2 on 2024-03-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0015_remove_customuser_profile_image_customuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='cnic',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='blog-post-image'),
        ),
    ]
