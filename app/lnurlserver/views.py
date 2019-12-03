from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello world ! ")

def about(request):
    print(request)
    # code to parse the secret, and check it against the db
    # render an HTTP response with the amount
    return HttpResponse("About")