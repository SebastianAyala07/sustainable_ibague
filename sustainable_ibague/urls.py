"""sustainable_ibague URL Configuration

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
import persons
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from sustainable_ibague import settings

urlpatterns = [
    path('', include('core.urls')),
    path('', include('persons.urls')),
    path('', include('monu.urls')),
    path('admin/', admin.site.urls),
    re_path(r'(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
