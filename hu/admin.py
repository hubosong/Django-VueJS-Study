# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hu.models import *

class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'category', 'color')
    list_display_links = ('id', 'name')
    list_per_page = 10
    ordering = ['id']
admin.site.register(Pictures, PicturesAdmin)

class PicturesCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    ordering = ['id']
admin.site.register(PicturesCategory, PicturesCategoryAdmin)

class PicturesColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color')
    ordering = ['id']
admin.site.register(PicturesColor, PicturesColorAdmin)

class YoutubeCodesAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')
    ordering = ['id']
admin.site.register(YoutubeCodes, YoutubeCodesAdmin)