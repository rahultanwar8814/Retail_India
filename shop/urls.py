from django.contrib import admin
from django.urls import path
from . import views, models

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.index2,name="bnm"),
    path('signup2',views.loginUser,name="bnm2"),
    path('logout',views.logoutUser, name="logout"),
    path('about', views.about, name="about2"),
    path('help', views.help, name="help2"),
    path('helpmassage',models.helpm,name="massage"),
    path('order2', models.oderupdate, name="oderupdate2"),
    path('other2',views.other, name="other22"),


]
