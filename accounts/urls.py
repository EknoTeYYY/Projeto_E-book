from django.urls import path
from . import views

urlpatterns =[
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.cadastrar, name ='cad'),
    path('logout/', views.user_logout, name='logout')

]