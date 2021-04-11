# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import re_path

from orders import views

urlpatterns = [
    re_path(r'^orders/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.OrderView.as_view(), name='orders'),
]
