from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to your Personal Finance Tracker!")

def about(request):
    return HttpResponse("Welcome to the about page!")