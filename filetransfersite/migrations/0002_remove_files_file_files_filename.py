# Generated by Django 4.0.4 on 2022-06-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filetransfersite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file',
        ),
        migrations.AddField(
            model_name='files',
            name='fileName',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
    ]
