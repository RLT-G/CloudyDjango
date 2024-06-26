# Generated by Django 4.2.5 on 2024-04-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm_site', '0013_tracks_unl_and_exc_link_tracks_waw_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedtrack',
            name='contract',
            field=models.FileField(blank=True, null=True, upload_to='uploads/contracts/'),
        ),
        migrations.AddField(
            model_name='purchasedtrack',
            name='track_license',
            field=models.CharField(blank=True, choices=[('WAV', 'Wav license'), ('UNLIMITED', 'Unlimited license'), ('EXCLUSIVE', 'Exclusive license')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='banners',
            name='link',
            field=models.URLField(default='http://cloudymotion.com/store', verbose_name='HREF'),
        ),
    ]
