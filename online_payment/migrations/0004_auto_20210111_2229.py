# Generated by Django 3.1.5 on 2021-01-11 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_payment', '0003_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='time',
            new_name='address',
        ),
    ]
