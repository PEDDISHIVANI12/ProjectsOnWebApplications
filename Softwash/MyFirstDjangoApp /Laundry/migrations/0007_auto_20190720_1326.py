# Generated by Django 2.2.2 on 2019-07-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laundry', '0006_auto_20190719_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='laundry',
            name='pickup_flat',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laundry',
            name='pickup_locality',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laundry',
            name='pickup_pincode',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
