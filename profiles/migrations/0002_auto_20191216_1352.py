# Generated by Django 2.2.4 on 2019-12-16 08:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 12, 16, 8, 22, 19, 197594, tzinfo=utc)),
        ),
    ]
