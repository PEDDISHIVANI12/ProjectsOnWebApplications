# Generated by Django 2.2.2 on 2019-07-20 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0010_auto_20190720_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laundry',
            name='delivery_slot',
        ),
        migrations.RemoveField(
            model_name='laundry',
            name='pickup_slot',
        ),
    ]
