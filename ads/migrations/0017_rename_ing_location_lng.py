# Generated by Django 4.1.6 on 2023-02-13 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0016_remove_ad_author_instance_remove_ad_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='ing',
            new_name='lng',
        ),
    ]
