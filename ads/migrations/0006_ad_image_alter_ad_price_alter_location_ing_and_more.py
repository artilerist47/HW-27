# Generated by Django 4.1.6 on 2023-02-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_ad_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='ing',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.PositiveIntegerField(),
        ),
    ]
