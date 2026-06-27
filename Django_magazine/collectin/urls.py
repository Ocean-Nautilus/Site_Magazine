from django.urls import path
from . import views

urlpatterns = [
    path('', views.collections_list, name='collections'),
]