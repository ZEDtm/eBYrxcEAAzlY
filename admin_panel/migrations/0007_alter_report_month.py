# Generated by Django 5.0.6 on 2024-05-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='month',
            field=models.CharField(verbose_name='Месяц'),
        ),
    ]