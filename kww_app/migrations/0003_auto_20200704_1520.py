# Generated by Django 3.0.4 on 2020-07-04 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kww_app', '0002_auto_20200704_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectparticipationissue',
            name='technologies',
        ),
        migrations.AddField(
            model_name='projectparticipationissue',
            name='technology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='kww_app.Technology'),
        ),
    ]
