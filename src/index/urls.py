from django.urls import path
from . import views as i


urlpatterns = [
    path('', i.index),
    path("test", i.test, name='test')
]