from django.urls import path

from .views import index_view, detail_view, create_view, update_view, delete_view

app_name = 'siswa'
urlpatterns = [
    path('', index_view, name="index"),
    	# route untuk halaman detail task
    path('detail/<int:siswa_id>', detail_view, name='detail'),
     # url untuk halaman tambah task
    path('create/', create_view, name='create'),
    # url untuk halaman ubah task
    path('update/<int:siswa_id>', update_view, name='update'),
    # url untuk menghapus task
    path('delete/<int:siswa_id>', delete_view, name='delete')
    
]