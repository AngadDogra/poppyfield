from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world, this is a poppy field and this is another change!")

