# Generated by Django 3.1.3 on 2020-11-18 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0004_type_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyuser',
            old_name='contact_person',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='company_name',
        ),
    ]