# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(Properties, MPTTModelAdmin)
admin.site.register(Address)
