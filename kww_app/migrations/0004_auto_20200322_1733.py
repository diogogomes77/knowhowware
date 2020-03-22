# Generated by Django 3.0.4 on 2020-03-22 17:33

from django.db import migrations, models
import minio_storage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('kww_app', '0003_auto_20200317_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='photo',
            field=models.ImageField(null=True, storage=minio_storage.storage.MinioMediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='projects/files/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/images/'),
        ),
    ]
