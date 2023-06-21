from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('compinfo/<str:pk>/', views.compinfo, name="compinfo"),
    path('createcomp/', views.create_competition, name="create-comp"),
    path('updatecomp/<str:pk>/', views.update_competition, name="update-comp"),
    path('delete/<str:pk>/', views.delete_page, name="delete"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_user, name="register_page"),
    path('logout/', views.logout_user, name="logout_user"),
    path('user/<str:pk>', views.user_profile, name="user_profile"),
    path('delete_comment/<str:pk>/', views.delete_comment, name="delete_comment"),
    path('register_comp/<str:pk>/', views.register_competition, name="register_comp"),
]