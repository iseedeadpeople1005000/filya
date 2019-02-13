from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'login/', views.login),
    re_path(r'logout/', views.out),
    re_path(r'register/', views.sign)
]