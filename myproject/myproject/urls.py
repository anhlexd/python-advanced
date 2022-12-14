"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    # path('user-auth/', include('user_auth.urls')),
    # path('file-upload/',include('file_uploader.urls')),
    # path('form-from-model/',include('form_from_model.urls')),
    path('asm-04',include('asm_04.urls')),
    path('registration',include('registration.urls')),
    path('pagination',include('pagination.urls')),
    path('adv-temp/',include('adv_temp.urls')),
    path('redis-cache/',include('redis_cache.urls')),
    path('login/',include('login.urls')), 
    path('members/',include('members.urls')),
  
]
