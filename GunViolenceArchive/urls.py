from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    #include("GunViolenceArchive.urls")

    url(r'^form/$', views.gv_form),
    url(r'^abc/$', views.gv_form),
]