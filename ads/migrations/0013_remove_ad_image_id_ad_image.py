# Generated by Django 4.1.6 on 2023-02-13 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0012_ad_image_id_alter_ad_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='image_id',
        ),
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ads.media'),
        ),
    ]
