# Generated by Django 4.2.5 on 2024-03-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm_site', '0009_tracks_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='description',
            field=models.CharField(default='Produced by @Cloudymotion4life. Only high quality beats for you💎', max_length=256, verbose_name='Track description'),
        ),
    ]
