# Generated by Django 2.2.18 on 2023-04-02 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_userfollow_follow_to_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInbux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.CharField(max_length=256)),
                ('operator', models.CharField(max_length=256)),
                ('action', models.CharField(max_length=256)),
                ('url', models.TextField()),
                ('detail', models.TextField()),
                ('add_time', models.DateTimeField(default=datetime.datetime(2023, 4, 2, 20, 51, 43, 301832))),
                ('is_read', models.BooleanField(default=0)),
            ],
        ),
    ]
