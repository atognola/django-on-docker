from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name='lnurlserver-home'),
    path("about", views.about, name='lnurlserver-home'),
]
