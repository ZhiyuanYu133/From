# Generated by Django 2.2.18 on 2023-04-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20230402_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinbux',
            name='action_model',
            field=models.CharField(default='UserFriends', max_length=100),
        ),
        migrations.AddField(
            model_name='userinbux',
            name='source_id',
            field=models.CharField(default="", max_length=100),
        ),
    ]