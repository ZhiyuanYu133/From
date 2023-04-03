# Generated by Django 4.2 on 2023-04-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20230402_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('type', models.CharField(default='node', editable=False, max_length=255)),
                ('host', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Node',
            },
        ),
        migrations.AlterModelOptions(
            name='userinbux',
            options={'ordering': ['-add_time', '-is_read']},
        ),
    ]