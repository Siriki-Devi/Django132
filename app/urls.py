from django.urls import path
from . import views
urlpatterns = [
    path('', views.form, name='home'),       
    path('form/', views.form, name='form'),  
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]