# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='\u76f8\u518c\u540d')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': '\u76f8\u518c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('image', models.ImageField(upload_to=b'photos', verbose_name='\u7167\u7247')),
                ('caption', models.CharField(max_length=250, verbose_name='\u5b57\u5e55', blank=True)),
                ('item', models.ForeignKey(to='photo.Item')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': '\u7167\u7247',
            },
            bases=(models.Model,),
        ),
    ]
