from django.http import HttpResponse


def views(request):
    return HttpResponse('index')
