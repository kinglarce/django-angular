# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-21 02:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180821_0948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoElements',
            new_name='ToDo',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='todo_text',
            new_name='text',
        ),
    ]
