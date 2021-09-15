from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='role'),
    path('create', views.create_view, name='create'),
    path('detail/<int:role_id>', views.detail_view, name='detail'),
     path('update/<int:role_id>', views.update_view, name='update'),
     path('delete/<int:role_id>', views.delete_view, name='delete')
]