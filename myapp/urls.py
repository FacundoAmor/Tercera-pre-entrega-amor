# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la vista de inicio
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('search_books/', views.search_books, name='search_books'),
]

