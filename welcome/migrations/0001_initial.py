# Generated by Django 4.1.7 on 2023-03-15 16:39

import django.contrib.postgres.fields
from django.db import migrations, models
import welcome.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=2), default=welcome.models.df, size=3), default=welcome.models.df, size=3)),
                ('isLogin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
