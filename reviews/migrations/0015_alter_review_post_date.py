# Generated by Django 4.0.4 on 2022-05-05 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_alter_review_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 16, 10, 16, 715229), verbose_name='Date of Review'),
        ),
    ]
