from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('login/', views.login,name='login'),
    path('', views.index),
    path('about/', views.about),
    path('contactus/', views.contactus,name='contactus'),
    path('signup/', views.signup,name='signup'),
    path('userlogout/', views.userlogout,name='userlogout'),
    path('profile/', views.profile,name='profile'),
    path('updateprofile/', views.updateprofile),
    path('basket' , views.basket),
    path('checkout/', views.checkout),
    path('removeitem/<int:id>',views.removeitem),
    path('finalbill/' ,views.finalbill),
]
