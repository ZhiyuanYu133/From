# Generated by Django 4.2 on 2023-04-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0010_alter_posts_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='type',
            field=models.CharField(default='post', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='uuid',
            field=models.CharField(default='41118620-8836-4c67-b316-82570d1da28f', max_length=255, unique=True),
        ),
    ]
