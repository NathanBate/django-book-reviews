from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pkg_resources import require
from taggit.managers import TaggableManager
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Review(models.Model):
    post_date = models.DateField(
        'Date of Review',
    )
    post_slug = models.CharField("Slug", max_length=255, null=True)

    review_preview_text = models.TextField(
        'Preview Text',
        max_length=255, 
        default="",
        null=True,
        help_text="Max 255 characters"
    )
    book_title = models.CharField("Title", max_length=255)
    book_subtitle = models.CharField("Subtitle", max_length=255, blank=True, null=True)
    book_author = models.CharField("Author",max_length=255, blank=True, null=True)

    # cover image with its transformations
    book_cover_image = models.ImageField("Cover Image",upload_to='images/', default="", blank=True, null=True)
    book_cover_thumbnail = ImageSpecField([ResizeToFill(200,292)], source='book_cover_image', format='JPEG',
                                          options={'quality': 75})

    book_star_rating = models.IntegerField(
        "Star Rating",
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    book_review_body_text = models.TextField("Review Text", blank=True, null=True)
    topic_tags = TaggableManager("Topic Tags", blank=True)

    def __str__(self):
        if len(self.book_subtitle) > 0: 
            return self.book_title + ": " + self.book_subtitle
        else:
            return self.book_title


    @admin.display(        
        ordering='book_title',
        description='Title',
    )
    def full_title(self) -> str: 
        if self.book_subtitle != None:
            return self.book_title + ": " + self.book_subtitle
        else:
            return self.book_title

