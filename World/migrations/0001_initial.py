# Generated by Django 4.1.2 on 2022-11-08 12:55

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=50)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name='Population 2005')),
                ('fips', models.CharField(max_length=2, null=True, verbose_name='FIPS Code')),
                ('iso2', models.CharField(max_length=2, verbose_name='2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name='3 Digit ISO')),
                ('un', models.IntegerField(verbose_name='United Nations Code')),
                ('region', models.IntegerField(verbose_name='Region Code')),
                ('subregion', models.IntegerField(verbose_name='Sub-Region Code')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
