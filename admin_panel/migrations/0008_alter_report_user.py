# Generated by Django 5.0.6 on 2024-05-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_alter_report_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.CharField(max_length=400, verbose_name='Пользователь'),
        ),
    ]
