# Generated by Django 3.2 on 2021-05-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reconcile', '0016_remove_trxrightcorrespodent_idpaiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='trxrightcorrespodent',
            name='idpaiment',
            field=models.CharField(default=-1, max_length=200),
            preserve_default=False,
        ),
    ]
