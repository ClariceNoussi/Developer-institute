"""plant_research URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from accounts import views
#from . import views
from django.conf.urls.static import static
from plant_research import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('plants/', include('plants.urls')),
    path('products/', include('produits.urls')),
    path('contact/', include('contact.urls')),
    path('forum/', include('forum.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
