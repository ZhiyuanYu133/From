# Generated by Django 2.2.18 on 2023-04-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(default=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profileImage',
            field=models.ImageField(blank=True, default='profile_pics/happy-face.png', upload_to='profile_pics'),
        ),
    ]
