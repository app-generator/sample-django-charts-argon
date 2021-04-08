# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict
from django import template

from app.forms import OrderForm
from app.models import Order
from app.utils import set_pagination, form_validation_error


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('dashboard.html')

    context['orders'], context['info'] = set_pagination(request, Order.objects.all().order_by('-id'), item_numer=10)
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@method_decorator(login_required(login_url='login'), name='dispatch')
class OrderView(View):
    context = {}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            self.context['template'] = self.get_create_form(pk)

        return JsonResponse(self.context)

    def post(self, request, pk=None, action=None):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            item = render_to_string('orders/row_item.html', {'order': order})

            response = {'valid': 'success', 'message': 'order created successfully.', 'item': item}
        else:
            response = {'valid': 'error', 'message': form_validation_error(form)}
        return JsonResponse(response)

    def put(self, request, pk=None, action=None):
        order = self.get_object(pk)
        form = OrderForm(QueryDict(request.body), instance=order)
        if form.is_valid():
            order = form.save()
            item = render_to_string('orders/row_item.html', {'order': order})

            response = {'valid': 'success', 'message': 'order updated successfully.', 'item': item}
        else:
            response = {'valid': 'error', 'message': form_validation_error(form)}

        return JsonResponse(response)

    def get_create_form(self, pk=None):
        form = OrderForm()
        if pk:
            form = OrderForm(instance=self.get_object(pk))
        return render_to_string('orders/modal_form.html', {'form': form})

    def get_object(self, pk):
        order = Order.objects.get(id=pk)
        return order
