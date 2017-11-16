import re
from django.forms import ValidationError
from django.conf import settings
from django.conf.urls import include, url
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.db import connection, models
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.generic import DetailView, ListView, TemplateView




# accounts/urls.py

urlpatterns += [
    url(r'^signup/$', views.signup, name='signup'),
]

def signup(req)
