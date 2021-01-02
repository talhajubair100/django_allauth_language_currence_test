# Generated by Django 3.1.3 on 2020-11-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0008_post_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default=6.0, max_digits=5),
            preserve_default=False,
        ),
    ]
