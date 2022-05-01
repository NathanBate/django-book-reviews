from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Review

class IndexView(generic.ListView):
    template_name = "reviews/index.html"
    context_object_name = "reviews_list"

    def get_queryset(self):
        """Return the last five book reviews"""
        return Review.objects.order_by('-post_date')[:5]


class DetailView(generic.DetailView):
    model = Review
    template_name = 'reviews/review.html'
