from django.http import HttpResponse


def base_view(request):
    return HttpResponse("Hello World from babytracker API")
