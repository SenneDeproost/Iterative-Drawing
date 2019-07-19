from django.urls import path

from . import views

urlpatterns = [
    path("", views.training, name='training'),
    path("get_case/<int:index>/", views.get_case, name="get_case"),
]
