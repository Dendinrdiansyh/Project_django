from django.urls import path
 
from uploadfileapp import views
 
app_name = 'uploadfileapp'
 
urlpatterns = [
 
    # uploadfileapp/
    path('', views.HomeView.as_view(),name='home' ),
 
    # uploadifileapp/register
    path('register/', views.UserEntry.as_view(), name='user-entry'),
 
]