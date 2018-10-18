# Generated by Django 2.1.2 on 2018-10-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20181018_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='total',
            field=models.DecimalField(decimal_places=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=12),
        ),
    ]
