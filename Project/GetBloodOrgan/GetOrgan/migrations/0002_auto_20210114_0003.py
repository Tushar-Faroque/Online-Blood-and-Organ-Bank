# Generated by Django 3.1.5 on 2021-01-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetOrgan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getorgan',
            name='address',
            field=models.CharField(max_length=1200, null=True),
        ),
        migrations.AlterField(
            model_name='getorgan',
            name='bloodtype',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='getorgan',
            name='organname',
            field=models.CharField(max_length=1200, null=True),
        ),
    ]
