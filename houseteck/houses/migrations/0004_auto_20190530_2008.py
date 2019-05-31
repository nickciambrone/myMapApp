# Generated by Django 2.2.1 on 2019-05-30 20:08

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_auto_20190530_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='baths',
        ),
        migrations.AddField(
            model_name='post',
            name='beds',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='house_pics'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 30, 20, 8, 27, 203897, tzinfo=utc)),
        ),
    ]
