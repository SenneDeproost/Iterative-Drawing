from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index),
    path("test", views.test, name='test'),
    path("register", include('form.urls'), name='register')
]