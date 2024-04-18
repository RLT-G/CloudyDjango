# Generated by Django 4.2.5 on 2024-04-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm_site', '0015_nosigncontracts_signcontracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorreport',
            name='description',
            field=models.TextField(max_length=8196, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='errorreport',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='errorreport',
            name='subject',
            field=models.CharField(blank=True, max_length=256, verbose_name='Subject'),
        ),
    ]