# Generated by Django 3.0.4 on 2020-07-19 13:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kww_app', '0012_auto_20200719_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
