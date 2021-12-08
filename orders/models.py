# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import datetime

from django.db import models
from django.db.models import Sum, Count, Max
from django.template.defaultfilters import date


class Order(models.Model):
    MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}

    product_name = models.CharField(max_length=40)
    price = models.IntegerField()
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    @classmethod
    def total_info(cls):
        return cls.objects.aggregate(total_sales=Sum('price'), total_orders=Count('id'), peek_sale=Max('price'))

    @classmethod
    def best_month(cls):
        res = {}
        month_price = cls.objects.values_list('created_time__month').annotate(total=Sum('price'))
        if month_price:
            res['month'], res['price'] = max(month_price, key=lambda i: i[1])
            res['month_name'] = date(datetime.date(datetime.datetime.now().year, month=res['month'], day=1), 'F')
        return res

    @classmethod
    def orders_month_report(cls):
        now = datetime.datetime.now()

        month_val = now.month + 1

        # Limit the upper value
        if month_val > 12:
            month_val = 12
        
        filter_params = {
            'created_time__date__gte': '{year}-{month}-{day}'.format(year=now.year - 1, month=month_val,
                                                                     day=now.day),
            'created_time__date__lte': now.date()
        }

        annotate_params = {
            'total_order': Count('id'),
            'total_price': Sum('price')
        }

        queryset = cls.objects.filter(**filter_params).values('created_time__year', 'created_time__month').annotate(**annotate_params)

        return list(queryset), [cls.MONTHS[data.get('created_time__month')] for data in queryset]
