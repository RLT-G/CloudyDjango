# Generated by Django 4.2.5 on 2024-04-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm_site', '0016_alter_errorreport_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorreport',
            name='email',
            field=models.CharField(blank=True, max_length=256, verbose_name='Email'),
        ),
    ]
