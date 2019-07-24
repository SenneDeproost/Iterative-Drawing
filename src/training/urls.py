from django.urls import path, include

from . import views
import sys
# Some ugly code in order to import module
#sys.path.append('../..')
#from testing import views as testviews

urlpatterns = [
    path("", views.training, name='training'),
    path("get_case/", views.get_case, name="get_case"),
    path("post_case/", views.post_case, name="post_case"),
    #path("next/", testviews.testing, name="next"),
]
