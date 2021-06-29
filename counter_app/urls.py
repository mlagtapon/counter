from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('plus_two', views.plus_two),
    path('destroy', views.destroy),
    path('num', views.num)
]