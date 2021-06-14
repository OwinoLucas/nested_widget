# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404, HttpResponseNotAllowed
from .forms import *
from .models import *


# Create your views here.
def home(request):
    properties = Properties.objects.all()
    if request.method == 'POST':
        p_form = PropertyForm(request.POST)
        form = AddressForm(request.POST)
        if p_form.is_valid() and form.is_valid():
            p_form.save()
            form.save()
            message.success(
                request, 'post created successfully!')
            return redirect('home')
    else:
        p_form = PropertyForm()
        form = AddressForm()

    context = {'properties': properties,
               'p_form': p_form,
               'form': form
               }
    return render(request, 'index.html', context)

# def single_property(request,property):
#     property = get_object_or_404(Properties)
#     addresses = property.address.get()
#     if request.method == 'POST':
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             address = form.save(commit=False)
#             address.property = property
#             address.save()
#             message.success(
#                 request, 'post created successfully!')
#             return redirect('home')
#     else:
#         form = AddressForm()

#     context = {'property': property,
#                 'form':form
#     }
#     return render(request, 'property.html', context)
