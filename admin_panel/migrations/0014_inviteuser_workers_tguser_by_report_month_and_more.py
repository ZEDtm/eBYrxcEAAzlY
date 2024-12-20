# Generated by Django 5.0.6 on 2024-06-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0013_tguser_address_registration_tguser_bank_bik_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inviteuser',
            name='workers',
            field=models.PositiveIntegerField(null=True, verbose_name='Кол-во оборудования'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='by_report_month',
            field=models.CharField(max_length=255, null=True, verbose_name='Отчет за месяц'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='default_cost',
            field=models.PositiveBigIntegerField(default=900, verbose_name='Стоимость по умолчанию'),
        ),
        migrations.AddField(
            model_name='tguser',
            name='workers',
            field=models.PositiveBigIntegerField(default=1, verbose_name='Количество оборудования'),
            preserve_default=False,
        ),
    ]
