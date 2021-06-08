# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# import datetime as dt

# Create your models here.


class Properties(MPTTModel):
    name = models.CharField(max_length=32)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    properties_link = models.ManyToManyField(Properties, blank=True, default=None,
                                             )
