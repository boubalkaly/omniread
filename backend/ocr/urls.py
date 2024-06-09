from django.urls import path
from . import views

urlpatterns = [
    path('', views.ocr_view, name='ocr_view'),
    path('/login', views.login, name='login'),
    path('/signup', views.signup, name='signup'),
    path('/logout', views.logout, name='logout'),
]
