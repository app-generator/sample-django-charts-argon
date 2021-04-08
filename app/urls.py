# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    path('', views.index, name='home'),  # The home page
    re_path(r'^orders/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.OrderView.as_view(), name='orders'),

    # Matches any html file
    re_path(r'^.*\.html', views.pages, name='pages'),
]
