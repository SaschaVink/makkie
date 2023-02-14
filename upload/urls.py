from django.contrib import admin
from django.urls import path
from .import views 


urlpatterns = [
	path('upload', views.upload, name="upload"),
	path('update-activity/<str:pk>/', views.updateactivity, name="update-activity"),
	path('uploadoverview', views.uploadoverview, name="uploadoverview"),

] 
