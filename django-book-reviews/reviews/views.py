from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def review(request, review_id):
    response = "This is the individual review page for %s"
    return HttpResponse(response % review_id)

