# Generated by Django 3.1.5 on 2021-01-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_payment', '0006_auto_20210112_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='bkash',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
