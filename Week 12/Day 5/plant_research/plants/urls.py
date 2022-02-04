from django.urls import path
from . import views
from django.conf.urls.static import static
from plant_research import settings

urlpatterns = [
    path('', views.plant, name='plants'),
    path('<int:family_id>/plants', views.plant, name='plant'),
    path('<int:plant_id>/plants', views.plant, name='plant'),
    path('<int:molecule_id>/plants', views.plant, name='plant'),
    path('<int:disease_id>/plants', views.plant, name='plant'),
    path('search/', views.search, name='search'),
    path('api/', views.api, name='api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
