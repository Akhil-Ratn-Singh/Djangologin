from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("",views.login, name="login"),
    path("userdetail/",views.userdetail,name="userdetail"),
    path("logout/",views.logout,name="logout"),
    ]
