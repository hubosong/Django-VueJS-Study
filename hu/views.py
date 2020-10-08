# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Pictures
from .models import YoutubeCodes


def home(request):
    pictures = Pictures.objects.all()
    youtubecodes = YoutubeCodes.objects.all()
    return render(request, 'index.html', {
        'pictures': pictures,
        'youtubecodes': youtubecodes
    })

def register(request):
    pictures = Pictures.objects.all().last()
    return render(request, 'register.html', {
        'pictures': pictures
    })
    

def register_images(request):
    if request.method == "POST":
        news = Pictures()
        news.image = request.FILES['image']
        news.save()
        # return redirect('register.html')
        return redirect(reverse('register') + '#images')
    else:
        return redirect('register')

def manage(request):
    pictures = Pictures.objects.all()
    return render(request, 'manage.html', {
        'pictures': pictures
    })
    
def update(request, pid = None):
    if pid is None:
        return redirect(reverse('manage') + '#images')
    else:
        picture = get_object_or_404(Pictures, id=pid)
        picture.image = request.FILES['image']
        picture.save()        
        return redirect(reverse('manage') + '#images')

def delete(request, pid = None):
    if pid is None:
        return redirect(reverse('manage') + '#images')
    else:
        pictures = get_object_or_404(Pictures, id=pid)
        pictures.delete()            
        return redirect(reverse('manage') + '#images')

def addcodes(request):
    # print(request.POST.get('code'))
    if request.method == "POST":
        youtubecodes = YoutubeCodes()
        youtubecodes.code = request.POST.get('code')
        youtubecodes.save()
        # return redirect('home')
        return redirect(reverse('home') + '#youtube')        
    else:
        youtubecodes = YoutubeCodes.objects.all()
        return redirect('home')

def delcodes(request, pid = None):
    if pid is None:
        return redirect('home')
    else:
        youtubecodes = get_object_or_404(YoutubeCodes, id=pid)
        youtubecodes.delete()            
        return redirect(reverse('home') + '#youtube')

