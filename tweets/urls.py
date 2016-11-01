from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
		url(r'^$', tweets_index, name='index'),
	]
