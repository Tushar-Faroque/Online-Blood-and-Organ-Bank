# Generated by Django 3.1.5 on 2021-01-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetORGAN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('bloodtype', models.CharField(max_length=10, null=True)),
                ('organname', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
