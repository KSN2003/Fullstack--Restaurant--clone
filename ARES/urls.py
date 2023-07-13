from django.urls import path
from ARES import views

app_name='ARES'

urlpatterns = [
    
    path('index', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('booking', views.booking, name = 'booking'),
    path('contact', views.contact, name = 'contact'),
    path('menu', views.menu, name = 'menu'),
    path('service', views.service, name = 'service'),
    path('testimonial', views.testimonial, name = 'testimonial'),
    path('team', views.team, name = 'team'),
    path('register', views.register, name = 'register'),
    
     #for user login and log out
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),
 
]
