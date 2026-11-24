from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),  
    path('index/', views.home, name='index'),                    
    path('about/', views.about, name='about'), 
    path('map/', views.map, name='map'), 
    path('view/', views.view, name='view'), 
    path('card/', views.card, name='card'), 
    path('pay/', views.pay, name='pay'), 
    path('profile/', views.profile, name='profile'), 
    path('registration/', views.registration, name='registration'), 
]