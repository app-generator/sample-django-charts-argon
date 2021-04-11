# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    path('', views.index, name='home'),  # The home page

    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
]
