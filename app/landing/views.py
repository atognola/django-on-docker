from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "landing/home.html")

def privacy(request):
    return render(request, "landing/privacy-policy.html")

def terms(request):
    return render(request, "landing/terms-conditions.html")