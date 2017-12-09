from django.urls import path
from . import views

app_name = 'coffee'

urlpatterns = [
    
    path('signup', views.usersignup, name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),

]
