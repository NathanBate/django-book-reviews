# Generated by Django 4.0.4 on 2022-05-15 00:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0016_alter_review_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='post_slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='post_date',
            field=models.DateField(verbose_name='Date of Review'),
        ),
    ]
