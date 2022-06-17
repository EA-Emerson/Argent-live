from django.contrib import admin
from django.urls import path
from . import views
# from . import forms
# the '.' means main directory

urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    # path("login/", views.loginPage, name="login"),
    # path("logout/", views.logoutUser, name="logout"),
]