# Generated by Django 3.2 on 2021-05-11 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reconcile', '0015_trxrightcorrespodent_idpaiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trxrightcorrespodent',
            name='idpaiment',
        ),
    ]