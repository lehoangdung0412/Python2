# Generated by Django 2.1.2 on 2018-10-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='postcode',
            field=models.IntegerField(),
        ),
    ]