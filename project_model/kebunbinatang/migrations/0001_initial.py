# Generated by Django 2.1.5 on 2019-02-11 08:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('berat', models.CharField(max_length=25)),
                ('umur', models.DateTimeField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('isi_kandang', models.CharField(max_length=255)),
                ('luas_kandang', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=255)),
                ('hari_berkunjung', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=255)),
                ('jadwal_jaga', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
