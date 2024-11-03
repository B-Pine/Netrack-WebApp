from django.template.context_processors import request
from django.urls import path
from realEstate_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name ='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name ='signup'),
    path('about', views.about, name='about'),
    path('properties', views.properties, name='properties'),    #for admin
    path('allproperty', views.all_property, name='all_property')  #for casual users

]