from django.contrib import admin
from django.urls import path, include # new

from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # new
    path('', Home.as_view(), name='home')
]
