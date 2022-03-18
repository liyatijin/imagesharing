from django.urls import path, include
from django.contrib import admin
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('addfile',views.addfile,name='addfile'),
]