from django.http import HttpResponse

def home_page(request):
    print("Home page requested")
    return HttpResponse("This is a home page")