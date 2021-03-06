# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-25 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import thresher.thresher


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door', models.CharField(max_length=50)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampleapp.Building')),
            ],
        ),
        migrations.CreateModel(
            name='ClockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_at', models.DateTimeField(auto_now_add=True)),
                ('clock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampleapp.Clock')),
            ],
        ),
        migrations.CreateModel(
            name='ClockOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_at', models.DateTimeField(auto_now_add=True)),
                ('clock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampleapp.Clock')),
                ('clock_in', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sampleapp.ClockIn')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_wage', models.FloatField(default=7.25)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_managed', to='sampleapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_first_name', thresher.thresher.CharFactField(max_length=500)),
                ('employee_last_name', thresher.thresher.CharFactField(max_length=500)),
                ('manager_first_name', thresher.thresher.CharFactField(max_length=500)),
                ('manager_last_name', thresher.thresher.CharFactField(max_length=500)),
                ('hourly_wage', thresher.thresher.FloatFactField()),
                ('in_at', thresher.thresher.DateTimeFactField()),
                ('out_at', thresher.thresher.DateTimeFactField()),
                ('door_in', thresher.thresher.DateTimeFactField()),
                ('door_out', thresher.thresher.DateTimeFactField()),
                ('building_name', thresher.thresher.CharFactField(max_length=500)),
                ('building_address1', thresher.thresher.CharFactField(max_length=500)),
                ('building_address2', thresher.thresher.CharFactField(max_length=500)),
                ('building_city', thresher.thresher.CharFactField(max_length=500)),
                ('building_state', thresher.thresher.CharFactField(max_length=500)),
                ('building_zipcode', thresher.thresher.CharFactField(max_length=500)),
                ('clock_out', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampleapp.ClockOut')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sampleapp.Job'),
        ),
        migrations.AddField(
            model_name='clockin',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sampleapp.Employee'),
        ),
    ]
