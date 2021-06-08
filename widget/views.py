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

    context = {'properties': properties}
    return render(request, 'index.html', context)
