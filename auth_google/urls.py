from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('superuser/', views.super_user, name='super_user')
]