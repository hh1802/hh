# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('sex', models.BooleanField(default=False)),
                ('icon', models.ImageField(upload_to='icons')),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'axf_users',
            },
        ),
        migrations.CreateModel(
            name='UserTicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=256)),
                ('out_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Usermodel')),
            ],
            options={
                'db_table': 'axf_users_ticket',
            },
        ),
    ]
