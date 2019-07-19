from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path("test", views.test, name='test'),
    path("register", include('form.urls'), name='register'),
    path("training", include('training.urls'), name="training"),
    path("testing", include('testing.urls'), name="testing")
]
