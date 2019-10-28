from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    re_path(r'^register/$', views.RegistroList.as_view()),
    re_path(r'^register/(?P<pk>\d+)$', views.RegistroDetail.as_view()),
]