# Generated by Django 3.1.5 on 2021-01-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('bloodtype', models.CharField(max_length=3)),
                ('date', models.IntegerField(max_length=10)),
                ('organlist', models.CharField(max_length=10)),
            ],
        ),
    ]
