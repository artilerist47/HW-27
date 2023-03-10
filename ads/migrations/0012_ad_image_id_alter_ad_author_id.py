# Generated by Django 4.1.6 on 2023-02-13 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ads.media'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ads.user'),
        ),
    ]
