from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('topics/', views.topicsPage, name="topics"),
]
