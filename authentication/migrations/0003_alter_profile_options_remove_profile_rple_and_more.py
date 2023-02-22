# Generated by Django 4.1.6 on 2023-02-20 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile_rple'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rple',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('moderator', 'moderator'), ('member', 'member'), ('unknown', 'unknown')], default='unknown', max_length=15),
        ),
    ]
