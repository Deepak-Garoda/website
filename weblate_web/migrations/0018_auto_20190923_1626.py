# -*- coding: utf-8 -*-
# Generated by Django 2.2.3 on 2019-09-23 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("weblate_web", "0017_auto_20190904_1340")]

    operations = [
        migrations.AddField(
            model_name="report",
            name="site_title",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="report",
            name="ssh_key",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
