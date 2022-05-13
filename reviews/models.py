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
        default=datetime.now(),
        
    )
    review_preview_text = models.TextField(
        'Preview Text',
        max_length=255, 
        default="", 
        help_text="Max 255 characters"
    )
    book_title = models.CharField("Title", max_length=255)
    book_subtitle = models.CharField("Subtitle", max_length=255, blank=True)
    book_author = models.CharField("Author",max_length=255, blank=True)

    # cover image with its transformations
    book_cover_image = models.ImageField("Cover Image",upload_to='images/', default="", blank=True)
    book_cover_thumbnail = ImageSpecField([ResizeToFill(200,292)], source='book_cover_image', format='JPEG',
                                          options={ 'quality': 75 })

    book_star_rating = models.IntegerField(
        "Star Rating",
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    book_review_body_text = models.TextField("Review Text", blank=True)
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
        if len(self.book_subtitle) > 0: 
            return self.book_title + ": " + self.book_subtitle
        else:
            return self.book_title

