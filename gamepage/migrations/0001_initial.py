# Generated by Django 4.1.6 on 2023-03-15 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatname', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(max_length=50000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('player', models.CharField(max_length=1000)),
                ('room', models.CharField(max_length=1000)),
            ],
        ),
    ]
