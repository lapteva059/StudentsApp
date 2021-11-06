# Generated by Django 3.0.1 on 2019-12-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191229_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinaccount',
            name='total_price_opt',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='суммарная оптовая стоимость'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='total_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='суммарная оптовая стоимость'),
        ),
    ]