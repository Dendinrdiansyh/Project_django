
from django.urls import path
from . import views


app_name = 'akun'

urlpatterns=[
    path('home/', views.index, name='home'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('special/',views.special,name='special'),
    path('',views.user_login,name='user_login'),
]