# Generated by Django 4.1.6 on 2023-02-15 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0024_remove_user_locations_user_locations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='locations',
            new_name='location',
        ),
    ]