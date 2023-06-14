from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('compinfo/<str:pk>/', views.compinfo, name="compinfo"),
    path('createcomp/', views.create_competition, name="create-comp"),
    path('updatecomp/<str:pk>/', views.update_competition, name="update-comp"),
    path('delete/<str:pk>/', views.delete_page, name="delete"),
]