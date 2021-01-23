# Generated by Django 3.1.2 on 2021-01-23 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_county',
            new_name='default_address',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_city',
            new_name='default_city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_street_address1',
        ),
    ]
