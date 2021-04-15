# Generated by Django 3.1.7 on 2021-04-14 10:43

from django.db import migrations, models
import django_bleach.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', django_bleach.models.BleachField(max_length=1000)),
                ('data', django_bleach.models.BleachField(max_length=1000)),
            ],
        ),
    ]