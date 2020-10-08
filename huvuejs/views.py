# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect, reverse
from hu.models import Pictures
from hu.models import PicturesCategory
from hu.models import PicturesColor
from hu.models import YoutubeCodes
from django.core.files.storage import FileSystemStorage

#used to generator ws
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import serialize
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.hashers import make_password, check_password

# def huvuejs(request):
#     return render(request, 'index_vuejs.html')

def huvuejs(request):
    return render(request, 'index_vuejs.html')

def huvuejs_register(request):
    return render(request, 'register_vuejs.html')    

def huvuejs_manage(request):
    return render(request, 'manage_vuejs.html')


def listImages(request):
    pictures = Pictures.objects.all()
    # print(">> ", pictures.count())
    s = serialize('json', pictures, fields=('id', 'name', 'image'))
    return JsonResponse({'result': json.loads(s)})  


# upload images from register-vuejs
def addImages(request):
    if request.method == "POST":
        images = Pictures()
        images.image = request.FILES['image']
        images.save()
        # return JsonResponse({'result': '200'})   
    
        pictures = [Pictures.objects.all().last()]
        # print(pictures.id)
        s = serialize('json', pictures, fields=('image'))
        tt = json.loads(s)
        print(tt[0]["fields"])
        return JsonResponse({'result': tt[0]["fields"]  })

    else:
        return JsonResponse({'result': '400'})   

def updImages(request, pid = None):
    print('upd')
    print('pid', pid)
    if request.method == "POST":
        images = Pictures()
        images.image = request.FILES['image']
        images.save()
        return JsonResponse({'result': '200'})
    else:
        return JsonResponse({'result': '400'})   

def delImages(request, pid = None):
    if pid is None:
        return JsonResponse({'result': '400'})
    else: 
        images = get_object_or_404(Pictures, id=pid)
        images.delete()
        return JsonResponse({'result': '200'})


def listYoutubeCodes(request):
    youtubecodes = YoutubeCodes.objects.all()
    s = serialize('json', youtubecodes, fields=('id', 'code'))
    return JsonResponse({'result': json.loads(s)})

def addYoutubeCodes(request):
    if request.method == "POST":
        res = json.loads(request.body)
        # print res['code']
        youtubecodes = YoutubeCodes()
        youtubecodes.code = str( res['code'])
        youtubecodes.save()
        return JsonResponse({'result': '200'})
    else:
        return JsonResponse({'result': '400'})

def delYoutubeCodes(request, pid = None):
    if pid is None:
        return JsonResponse({'result': '400'})
    else: 
        youtubecodes = get_object_or_404(YoutubeCodes, id=pid)
        youtubecodes.delete()
        return JsonResponse({'result': '200'})

def showCategory(request):
    category = PicturesCategory.objects.all()
    s = serialize('json', category, fields=('id', 'category'))
    return JsonResponse({'result': json.loads(s)})  

def showColor(request):
    colors = PicturesColor.objects.all()
    s = serialize('json', colors, fields=('id', 'color'))
    return JsonResponse({'result': json.loads(s)})  

def imagesByCategory(request):
    print(request)
    if not request.method == 'GET':
        return JsonResponse({'result': '400'})
    
    print(request.GET.get('category'))

    images = Pictures.objects.filter(category=request.GET.get('category'))

    s = serialize('json', images, fields=('id', 'name', 'image'))
    return JsonResponse({'result': json.loads(s)})  

def imagesByColor(request):
    if not request.method == 'GET':
        return JsonResponse({'result': '400'})
    
    images = Pictures.objects.filter(color=request.GET.get('color'))

    s = serialize('json', images, fields=('id', 'name', 'image'))
    return JsonResponse({'result': json.loads(s)})  
        
        
    