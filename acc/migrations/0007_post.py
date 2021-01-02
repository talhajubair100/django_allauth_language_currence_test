# Generated by Django 3.1.3 on 2020-11-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0006_delete_type_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('text_en_us', models.CharField(max_length=100, null=True)),
                ('text_bn', models.CharField(max_length=100, null=True)),
                ('discription', models.TextField()),
                ('discription_en_us', models.TextField(null=True)),
                ('discription_bn', models.TextField(null=True)),
            ],
        ),
    ]
