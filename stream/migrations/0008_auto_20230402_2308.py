# Generated by Django 2.2.18 on 2023-04-02 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0007_posts_friends_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='friends_public',
            new_name='is_friends_public',
        ),
    ]
