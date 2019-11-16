from django.urls import path
from . import views 

urlpatterns = [
	#path('', views.page,name="page"),
	path('<int:category_id>/',views.page,name="page")
	]