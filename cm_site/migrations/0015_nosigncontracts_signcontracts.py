# Generated by Django 4.2.5 on 2024-04-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm_site', '0014_purchasedtrack_contract_purchasedtrack_track_license_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoSignContracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wav_license', models.FileField(upload_to='uploads/contracts/temp/', verbose_name='Wav license contract')),
                ('unlimited_license', models.FileField(upload_to='uploads/contracts/temp/', verbose_name='Unlimited license contract')),
                ('exclusive_license', models.FileField(upload_to='uploads/contracts/temp/', verbose_name='Exclusive license contract')),
            ],
            options={
                'verbose_name': 'No Sign Contract',
                'verbose_name_plural': 'No Sign Contracts',
            },
        ),
        migrations.CreateModel(
            name='SignContracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wav_license', models.FileField(upload_to='uploads/contracts/temp/', verbose_name='Wav license contract')),
                ('unlimited_license', models.FileField(upload_to='uploads/contracts/temp/', verbose_name='Unlimited license contract')),
                ('exclusive_license', models.FileField(upload_to='uploads/contracts/temp/', verbose_name='Exclusive license contract')),
            ],
            options={
                'verbose_name': 'Sign Contract',
                'verbose_name_plural': 'Sign Contracts',
            },
        ),
    ]
