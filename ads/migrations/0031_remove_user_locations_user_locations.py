# Generated by Django 4.1.6 on 2023-02-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0030_remove_user_locations_user_locations'),
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
