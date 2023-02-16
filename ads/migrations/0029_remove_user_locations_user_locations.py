# Generated by Django 4.1.6 on 2023-02-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0028_remove_user_location_user_locations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='locations',
        ),
        migrations.AddField(
            model_name='user',
            name='locations',
            field=models.ManyToManyField(to='ads.location'),
        ),
    ]
