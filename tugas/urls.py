from django.urls import path

from .views import index_view, create_view, update_view, delete_view

urlpatterns= [
    path('', index_view, name="index"),
    path('create', create_view, name="create"),
    path('update/<int:tugas_id>', update_view, name="update"),
    path('delete/<int:tugas_id>', delete_view, name="delete")
    
    
]