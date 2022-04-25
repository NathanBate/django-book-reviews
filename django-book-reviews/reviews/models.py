from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    review_date = models.DateTimeField('date review was published')
    book_title = models.CharField(max_length=255)
    book_subtitle = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    book_star_rating = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    book_review = models.TextField()

class TopicTag(models.Model):
    book_review = models.ForeignKey(Review, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=255)
    topic_description = models.TextField

