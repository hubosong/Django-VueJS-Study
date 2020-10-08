# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect, reverse

def homeVueJS(request):
    return render(request, 'base.html')
