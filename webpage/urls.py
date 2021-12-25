from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/account/', views.account, name='account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
