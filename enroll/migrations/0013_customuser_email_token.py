# Generated by Django 5.0.2 on 2024-03-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0012_customuser_is_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_token',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
