# Generated by Django 2.2.5 on 2021-01-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonateORGAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=1200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('needblood', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
