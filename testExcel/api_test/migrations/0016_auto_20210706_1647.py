# Generated by Django 3.2.4 on 2021-07-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0015_auto_20210706_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='countCinetpay',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='countCinetpayAfter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='countOperator',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='countOperatorAfter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='diffCount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='diffCountAfter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='diffMontant',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='diffMontantAfter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='montantCinetpay',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='montantCinetpayAfter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='montantOperateur',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='montantOperateurAfter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
