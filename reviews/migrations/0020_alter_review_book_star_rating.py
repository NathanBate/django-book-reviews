# Generated by Django 4.0.4 on 2022-05-15 01:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_alter_review_book_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book_star_rating',
            field=models.IntegerField(default=3, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Star Rating'),
        ),
    ]
