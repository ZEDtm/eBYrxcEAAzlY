# Generated by Django 5.0.6 on 2024-06-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0012_inviteuser_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='address_registration',
            field=models.CharField(max_length=500, null=True, verbose_name='Адрес регистрации'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='bank_bik',
            field=models.CharField(max_length=255, null=True, verbose_name='БИК'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='bank_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название банка'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='corr_account',
            field=models.CharField(max_length=255, null=True, verbose_name='Корр. счет'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='date_passport',
            field=models.CharField(max_length=255, null=True, verbose_name='Дата выдачи паспорта'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='get_passport',
            field=models.CharField(max_length=500, null=True, verbose_name='Кем выдан паспорт'),
        ),
    ]
