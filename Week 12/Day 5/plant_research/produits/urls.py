from django.urls import path
from . import views


urlpatterns = [
    path('', views.produits, name='products'),
    path('<int:product_id>/products', views.product, name='product'),
    path('buy_product/<int:id>', views.buy, name='buy'),
    path('panier', views.show_panier, name='panier'),


]