from django.urls import path, include
from . import views 

urlpatterns = [
	path('overview', views.overview, name="overview"),
]