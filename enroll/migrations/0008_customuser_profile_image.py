# Generated by Django 5.0.2 on 2024-03-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_adminpermission_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
