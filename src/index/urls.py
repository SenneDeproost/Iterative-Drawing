from django.urls import path
from . import views
from ..form import views

urlpatterns = [
    path('', views.index),
    path("/test", views.test, name='test')
]