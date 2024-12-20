# Generated by Django 5.0.6 on 2024-05-22 18:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_yookassaconfig_alter_tguser_uniq_code_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='expire_date_subscribe',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата окончания платежа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tguser',
            name='subscribe',
            field=models.BooleanField(default=False, verbose_name='активная подписка'),
        ),
    ]
