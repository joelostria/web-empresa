from django.urls import path
from . import views 

urlpatterns = [
	#path('', views.page,name="page"),
	path('<int:page_id>/',views.page,name="page")
	]