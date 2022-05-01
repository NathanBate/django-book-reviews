# Generated by Django 4.0.4 on 2022-05-01 17:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_rename_review_date_review_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_cover_image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Cover Image'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book_author',
            field=models.CharField(max_length=255, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book_review_body_text',
            field=models.TextField(verbose_name='Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book_star_rating',
            field=models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Star Rating'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book_subtitle',
            field=models.CharField(max_length=255, verbose_name='Subtitle'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book_title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='review',
            name='post_date',
            field=models.DateTimeField(verbose_name='Date of Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_preview_text',
            field=models.TextField(default='', help_text='Max 255 characters', max_length=255, verbose_name='Preview Text'),
        ),
    ]
