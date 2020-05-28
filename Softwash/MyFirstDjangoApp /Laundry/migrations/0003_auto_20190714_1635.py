# Generated by Django 2.2.2 on 2019-07-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0002_auto_20190714_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='laundry',
            name='delivery_address',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laundry',
            name='details',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laundry',
            name='pickup_address',
            field=models.TextField(default=' ', max_length=500),
            preserve_default=False,
        ),
    ]
