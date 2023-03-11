from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('home', views.home, name="home"),
    path('playing', views.playing, name="playing"),
    path('reset', views.reset, name="reset")
]