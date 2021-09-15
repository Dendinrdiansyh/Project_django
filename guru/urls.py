from django.urls import path

from .views import index_view, detail_view, create_view, update_view, delete_view

app_name= 'guru'
urlpatterns = [
    path('', index_view, name='index'),
    path('detail/<int:guru_id>', detail_view, name='detail'),
    path('create/', create_view, name='create'),
    path('update/<int:guru_id>', update_view, name='update'),
    path('delete/<int:guru_id>', delete_view, name='delete')
    
]
