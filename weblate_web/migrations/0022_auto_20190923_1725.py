# -*- coding: utf-8 -*-
# Generated by Django 2.2.3 on 2019-09-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("weblate_web", "0021_auto_20190923_1724")]

    operations = [
        migrations.RenameField(
            model_name="subscription", old_name="status", new_name="package"
        )
    ]
