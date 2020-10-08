from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
        
    url(r'^register/', views.register, name='register'),
    url(r'^register_images/', views.register_images, name='register_images'),

    url(r'^manage/', views.manage, name='manage'),    
    url(r'^update/(?P<pid>\d+)/$', views.update, name='update'),
    url(r'^delete/(?P<pid>\d+)/$', views.delete, name='delete'),
    
    url(r'^addcodes/', views.addcodes, name='addcodes'),    
    url(r'^delcodes/(?P<pid>\d+)/$', views.delcodes, name='delcodes'),
]