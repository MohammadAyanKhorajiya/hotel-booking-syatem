# hotel/urls.py - Hotel app के URLs

from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # सभी कमरों की list
    path('rooms/', views.rooms_list, name='rooms'),
    
    # एक specific कमरे की details
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    
    # संपर्क पेज
    path('contact/', views.contact, name='contact'),
    
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
]
