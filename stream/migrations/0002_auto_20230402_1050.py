# Generated by Django 2.2.18 on 2023-04-02 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='count',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stream.Posts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='CommonMark',
            field=models.BooleanField(default=False),
        ),
    ]