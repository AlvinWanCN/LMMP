# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('src', models.CharField(max_length=64)),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
    ]
