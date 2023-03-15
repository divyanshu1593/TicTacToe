from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('home', views.home, name="home"),
    path('playing', views.playing, name="playing"),
    path('reset', views.reset, name="reset"),
    path('welcome', views.welcome, name="welcome"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('verify', views.verify, name="verify"),
    path('signup', views.signup, name="signup"),
    path('insertData', views.insertData, name="insertData"),
    path('aboutus', views.aboutus, name="aboutus")
]