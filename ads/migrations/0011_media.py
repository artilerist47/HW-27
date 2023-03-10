# Generated by Django 4.1.6 on 2023-02-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_delete_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Медиа',
                'verbose_name_plural': 'Медиа',
            },
        ),
    ]
