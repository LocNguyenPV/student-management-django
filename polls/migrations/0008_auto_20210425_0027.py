# Generated by Django 3.2 on 2021-04-24 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210425_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='modify_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 25, 0, 27, 58, 45104)),
        ),
    ]
