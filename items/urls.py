# items/urls.py
from django.urls import path
from django.contrib import admin
from items import views

urlpatterns = [
    path('create/', views.create_item, name='create_item'),
    path('', views.list_items, name='list_items'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    
]
