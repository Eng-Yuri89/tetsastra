# Generated by Django 4.0 on 2021-12-29 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0002_alter_blog_date_alter_blog_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'managed': True, 'ordering': ['title'], 'verbose_name': 'Ahmed'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
