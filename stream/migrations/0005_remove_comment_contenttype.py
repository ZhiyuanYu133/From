# Generated by Django 2.2.18 on 2023-04-02 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_auto_20230402_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='contentType',
        ),
    ]
