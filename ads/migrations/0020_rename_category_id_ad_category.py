# Generated by Django 4.1.6 on 2023-02-13 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0019_remove_ad_author_id_alter_ad_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='category_id',
            new_name='category',
        ),
    ]
