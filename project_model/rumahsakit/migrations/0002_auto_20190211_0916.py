# Generated by Django 2.1.5 on 2019-02-11 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rumahsakit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dokter',
            old_name='name',
            new_name='nama',
        ),
    ]
