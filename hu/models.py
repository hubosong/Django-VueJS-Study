# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class YoutubeCodes(models.Model):
    code = models.CharField(max_length=255)    

class PicturesCategory(models.Model):
    category = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.category)

class PicturesColor(models.Model):
    color = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.color)

class Pictures(models.Model):
    name = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/%Y/%m', null = True, blank = True)
    category = models.ForeignKey('PicturesCategory', on_delete=models.CASCADE, default=3)
    color = models.ForeignKey('PicturesColor', on_delete=models.CASCADE, default=4)
    



