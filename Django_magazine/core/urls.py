from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('favorites/', views.favorites, name='favorites'),
    path('catalog/', views.catalog, name='catalog'),
    path('collections/', views.collections_list, name='collections'),
    path('product/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
]