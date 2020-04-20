from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hdvideos/', views.hdvideos, name='hdvideos'),
    path('contactus/', views.contactus, name='contactus'),
    path('sites/', views.sites, name='sites'),
    path('categories/', views.categories, name='categories'),
    path('music/', views.music, name='music'),
    path('upcoming/', views.upcoming, name='upcoming')
]
