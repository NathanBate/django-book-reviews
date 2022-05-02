from django.contrib import admin

# Register your models here.

from .models import Review


class ReviewAdmin(admin.ModelAdmin):    

    fieldsets = [
        (None,              {'fields': ['post_date','review_preview_text']}),
        ('Book Info',       {'fields': ['book_cover_image','book_title','book_subtitle', 'book_author']}),
        ('My Review',       {'fields': ['book_star_rating', 'book_review_body_text', 'topic_tags']})
    ]

    list_display = ('full_title', 'book_author', 'book_star_rating', 'topic_tags')


admin.site.register(Review, ReviewAdmin)