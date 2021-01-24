# Generated by Django 3.1.3 on 2021-01-24 11:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('b_code', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 1, 24, 11, 41, 21, 905970, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default='01735700187', max_length=14),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
