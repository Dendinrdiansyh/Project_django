from django.urls import path

# import my_view from todo Application
from .views import index_view, detail_view, create_view, update_view, delete_view

app_name = 'mapel'
urlpatterns = [
    path('', index_view, name="index"),
    path('detail/<int:mapel_id>', detail_view, name="detail"),
      # url untuk halaman tambah task
    path('create', create_view, name='create'),
     # url untuk halaman ubah task
    path('update/<int:mapel_id>', update_view, name='update'),
     # url untuk menghapus task
    path('delete/<int:mapel_id>', delete_view, name='delete'),
]