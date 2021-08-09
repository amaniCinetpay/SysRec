# Generated by Django 3.2 on 2021-06-14 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=512)),
                ('account', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50, null=True, unique=True)),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=512)),
                ('dateDebut', models.DateTimeField(verbose_name='Date de début')),
                ('dateFin', models.DateTimeField(verbose_name='Date de fin')),
                ('etat', models.CharField(choices=[('CREATION', 'CREATION'), ('ENCOURS', 'EN COURS'), ('TERMINEE', 'TERMINEE'), ('VALIDEE', 'VALIDEE')], default='CREATION', max_length=50)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now=True)),
                ('operateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.operateur')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrxCinetpay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(max_length=200)),
                ('cpm_payment_date', models.CharField(max_length=200)),
                ('marchand', models.CharField(max_length=200)),
                ('EmailMarchand', models.CharField(max_length=200)),
                ('NomDuService', models.CharField(max_length=200)),
                ('cpm_trans_id', models.CharField(max_length=200)),
                ('cpm_site_id', models.CharField(max_length=200)),
                ('cpm_amount', models.CharField(max_length=200)),
                ('cpm_currency', models.CharField(max_length=200)),
                ('payment_method', models.CharField(max_length=200)),
                ('cel_phone_num', models.CharField(max_length=200)),
                ('cpm_trans_status', models.CharField(max_length=200)),
                ('cpm_payid', models.CharField(max_length=200)),
                ('cpm_custom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TrxSuccessCinetpay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(max_length=200)),
                ('cpm_payment_date', models.CharField(max_length=200)),
                ('marchand', models.CharField(max_length=200)),
                ('EmailMarchand', models.CharField(max_length=200)),
                ('NomDuService', models.CharField(max_length=200)),
                ('cpm_trans_id', models.CharField(max_length=200)),
                ('cpm_site_id', models.CharField(max_length=200)),
                ('cpm_amount', models.CharField(max_length=200)),
                ('cpm_currency', models.CharField(max_length=200)),
                ('payment_method', models.CharField(max_length=200)),
                ('cel_phone_num', models.CharField(max_length=200)),
                ('cpm_trans_status', models.CharField(max_length=200)),
                ('cpm_payid', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('cpm_custom', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxRightCorrespodentDdvaVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.CharField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('trans_id', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('created_atCorrespondent', models.CharField(max_length=200)),
                ('cel_phone_numCorrespondant', models.CharField(max_length=200)),
                ('AmountCorrespodent', models.CharField(max_length=200)),
                ('payment_methodCorrespondant', models.CharField(max_length=200)),
                ('StautTransactionCorrespondent', models.CharField(max_length=200)),
                ('cpm_trans_idCorrespondent', models.CharField(max_length=200)),
                ('cpm_customCorrespondent', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxRightCorrespodent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.CharField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('created_atCorrespondent', models.CharField(max_length=200)),
                ('cel_phone_numCorrespondant', models.CharField(max_length=200)),
                ('AmountCorrespodent', models.CharField(max_length=200)),
                ('payment_methodCorrespondant', models.CharField(max_length=200)),
                ('StautTransactionCorrespondent', models.CharField(max_length=200)),
                ('cpm_trans_idCorrespondent', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxreconciledDdvaVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('trans_id', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('created_atCorrespondent', models.CharField(max_length=200)),
                ('cel_phone_numCorrespondant', models.CharField(max_length=200)),
                ('AmountCorrespodent', models.CharField(max_length=200)),
                ('payment_methodCorrespondant', models.CharField(max_length=200)),
                ('StautTransactionCorrespondent', models.CharField(max_length=200)),
                ('cpm_trans_idCorrespondent', models.CharField(max_length=200)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('cpm_custom', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='Trxreconciled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.CharField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('created_atCorrespondent', models.CharField(max_length=200)),
                ('cel_phone_numCorrespondant', models.CharField(max_length=200)),
                ('AmountCorrespodent', models.CharField(max_length=200)),
                ('payment_methodCorrespondant', models.CharField(max_length=200)),
                ('StautTransactionCorrespondent', models.CharField(max_length=200)),
                ('cpm_trans_idCorrespondent', models.CharField(max_length=200)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('cpm_custom', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxOperateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('trans_id', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxNonereconciledDdvaVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('trans_id', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxNonereconciled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.CharField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('cpm_custom', models.CharField(max_length=200)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxFailedCinetpay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(max_length=200)),
                ('cpm_payment_date', models.CharField(max_length=200)),
                ('marchand', models.CharField(max_length=200)),
                ('EmailMarchand', models.CharField(max_length=200)),
                ('NomDuService', models.CharField(max_length=200)),
                ('cpm_trans_id', models.CharField(max_length=200)),
                ('cpm_site_id', models.CharField(max_length=200)),
                ('cpm_amount', models.CharField(max_length=200)),
                ('cpm_currency', models.CharField(max_length=200)),
                ('payment_method', models.CharField(max_length=200)),
                ('cel_phone_num', models.CharField(max_length=200)),
                ('cpm_trans_status', models.CharField(max_length=200)),
                ('cpm_payid', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('cpm_custom', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxDifferenceDdvaVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('trans_id', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxDifference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('trans_id', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxDdvaVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(max_length=200)),
                ('payid', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('trans_id', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='TrxCorrespondent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(max_length=200)),
                ('cpm_payment_date', models.CharField(max_length=200)),
                ('marchand', models.CharField(max_length=200)),
                ('EmailMarchand', models.CharField(max_length=200)),
                ('NomDuService', models.CharField(max_length=200)),
                ('cpm_trans_id', models.CharField(max_length=200)),
                ('cpm_site_id', models.CharField(max_length=200)),
                ('cpm_amount', models.CharField(max_length=200)),
                ('cpm_currency', models.CharField(max_length=200)),
                ('payment_method', models.CharField(max_length=200)),
                ('cel_phone_num', models.CharField(max_length=200)),
                ('cpm_trans_status', models.CharField(max_length=200)),
                ('cpm_payid', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('agent', models.CharField(max_length=200)),
                ('cpm_custom', models.CharField(max_length=200)),
                ('tache', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_test.tache')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
