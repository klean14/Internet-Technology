from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Rango says hey there partner!')

