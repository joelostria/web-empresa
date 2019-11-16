from django.urls import path
from . import views as nucleo

urlpatterns = [
    path('',nucleo.contact, name="contact"),
    
]
