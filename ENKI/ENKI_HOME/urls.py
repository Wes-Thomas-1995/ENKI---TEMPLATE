from . import views
from django.urls import path

urlpatterns =  [
    path('', views.Home_Page, name="home-page"),
    path('register/', views.Register, name="register"),
]