# Generated by Django 4.0 on 2021-12-29 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0003_alter_blog_options_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
