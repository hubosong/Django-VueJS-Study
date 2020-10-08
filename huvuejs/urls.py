from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.huvuejs, name='huvuejs'),
    
    url(r'^huvuejs_register/', views.huvuejs_register, name='huvuejs_register'),    
    url(r'^huvuejs_manage/', views.huvuejs_manage, name='huvuejs_manage'),

    url(r'^listImages/', views.listImages, name='listImages'),
    url(r'^addImages/', views.addImages, name='addImages'),
    url(r'^updImages/(?P<pid>\d+)/$', views.updImages, name='updImages'),
    url(r'^delImages/(?P<pid>\d+)/$', views.delImages, name='delImages'),

    url(r'^listYoutubeCodes/', views.listYoutubeCodes, name='listYoutubeCodes'),    
    url(r'^addYoutubeCodes/', views.addYoutubeCodes, name='addYoutubeCodes'),
    url(r'^delYoutubeCodes/(?P<pid>\d+)/$', views.delYoutubeCodes, name='delYoutubeCodes'),

    url(r'^showCategory/', views.showCategory, name='showCategory'),
    url(r'^showColor/', views.showColor, name='showColor'),
    url(r'^imagesByCategory/', views.imagesByCategory, name='imagesByCategory'),
    url(r'^imagesByColor/', views.imagesByColor, name='imagesByColor'),
    
    
]