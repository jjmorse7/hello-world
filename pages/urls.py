from django.urls import path

from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home"),
]
__author__ = "Jonathan Morse"
