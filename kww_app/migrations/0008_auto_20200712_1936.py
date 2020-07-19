# Generated by Django 3.0.4 on 2020-07-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kww_app', '0007_company_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.AddField(
            model_name='company',
            name='countries',
            field=models.ManyToManyField(to='kww_app.Country'),
        ),
    ]