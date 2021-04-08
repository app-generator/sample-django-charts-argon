# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Count, Max, F
from django.db.models.functions import TruncMonth
from django.template.defaultfilters import date


class Order(models.Model):
    product_name = models.CharField(max_length=40)
    price = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    @classmethod
    def total_info(cls):
        return cls.objects.aggregate(total_sales=Sum('price'), total_orders=Count('id'), peek_sale=Max('price'))

    @classmethod
    def best_month(cls):
        month_price = cls.objects.values_list('created_time__month').annotate(total=Sum('price'))
        month, price = max(month_price, key=lambda i: i[1])

        res = dict(
            month=month,
            price=price,
            month_name=date(datetime.date(datetime.datetime.now().year, month=10, day=1), 'F')
        )
        return res

    @classmethod
    def orders_month_report(cls):
        queryset = cls.objects.values('created_time__month').annotate(total_order=Count('id'), total_price=Sum('price'))
        return list(queryset)
