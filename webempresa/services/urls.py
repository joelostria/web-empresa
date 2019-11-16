
    
from django.urls import path
from . import views as service

urlpatterns = [
	path('', service.services,name="services")
	]