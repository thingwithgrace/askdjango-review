# blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^temp_study/$', views.temp_study)
]