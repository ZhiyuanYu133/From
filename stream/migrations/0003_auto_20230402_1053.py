# Generated by Django 2.2.18 on 2023-04-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_auto_20230402_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
