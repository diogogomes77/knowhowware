# Generated by Django 3.0.4 on 2020-07-12 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kww_app', '0003_auto_20200704_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='offboard',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='onboard',
        ),
        migrations.CreateModel(
            name='HasJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onboard', models.DateField(blank=True, null=True)),
                ('offboard', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kww_app.Company')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kww_app.Participant')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kww_app.Role')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='jobs',
            field=models.ManyToManyField(related_name='colaborators', through='kww_app.HasJob', to='kww_app.Company'),
        ),
    ]