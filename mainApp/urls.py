from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blank_index"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout")
]