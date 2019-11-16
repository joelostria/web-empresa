from django.urls import path
from . import views as blo

urlpatterns = [
	path('', blo.blog,name="blog"),
	path('category/<int:category_id>/',blo.category,name="category")
	]