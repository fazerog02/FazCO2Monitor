from django.urls import path
from . import views

urlpatterns = [
    path('date/', views.date),
    path('month/', views.month),
    path('year/', views.year),
    path('today/', views.today),
    path('archive', views.archive),
]