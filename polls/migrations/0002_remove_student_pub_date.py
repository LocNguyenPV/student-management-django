# Generated by Django 3.2 on 2021-04-14 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pub_date',
        ),
    ]