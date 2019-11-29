from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name='landing-home'),
    path("privacy-policy/", views.privacy, name='landing-privacy-policy'),
    path("terms/", views.terms, name='landing-terms'),
]