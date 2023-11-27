from django.urls import path

from . import views

urlpatterns = [
    path('', views.movies, name='movies'),
    path('add-movie/', views.addMovie, name='add-movie'),
    path('edit-movie/<str:pk>/', views.editMovie, name='edit-movie'),
    path('delete-movie/<str:pk>/', views.deleteMovie, name='delete-movie'),
]
