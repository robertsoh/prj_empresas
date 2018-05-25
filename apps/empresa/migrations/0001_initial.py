# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=15, verbose_name='RUC')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('nombre_comercial', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre comercial')),
                ('fecha_inscripcion', models.DateField(blank=True, null=True, verbose_name='Fecha inscripción')),
                ('estado', models.CharField(choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')], default='INACTIVO', max_length=10, verbose_name='Estado')),
                ('condicion', models.CharField(choices=[('HABIDO', 'Habido'), ('NOHABIDO', 'No habido')], default='HABIDO', max_length=10, verbose_name='Condición')),
                ('domicilio_fiscal', models.CharField(blank=True, max_length=255, null=True, verbose_name='Domicilio fiscal')),
            ],
        ),
        migrations.CreateModel(
            name='TipoContribuyente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, verbose_name='RUC')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='tipo_contribuyente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.TipoContribuyente', verbose_name='Tipo contribuyente'),
        ),
    ]
