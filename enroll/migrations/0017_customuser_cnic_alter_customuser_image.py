# Generated by Django 5.0.2 on 2024-03-15 10:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0016_remove_customuser_cnic_alter_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cnic',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
