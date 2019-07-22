from django.urls import path

from . import views

urlpatterns = [
    path("", views.training, name='training'),
    path("get_case/", views.get_case, name="get_case"),
    path("post_case/", views.post_case, name="post_case"),
]
