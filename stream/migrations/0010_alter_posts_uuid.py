# Generated by Django 4.2 on 2023-04-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0009_posts_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='uuid',
            field=models.CharField(default='505269b1-714e-4f71-a4a2-222918b50d5a', max_length=255, unique=True),
        ),
    ]