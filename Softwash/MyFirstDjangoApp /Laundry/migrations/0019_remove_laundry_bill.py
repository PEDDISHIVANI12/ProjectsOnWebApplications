# Generated by Django 2.2.2 on 2019-07-26 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0018_auto_20190726_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laundry',
            name='bill',
        ),
    ]
