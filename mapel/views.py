from django.shortcuts import redirect,render
from django.http import Http404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Mapel
from .forms import MapelForm
# Membuat View untuk halaman daftar task
def index_view(request):
    # Mengambil semua data task
    mapel = Mapel.objects.all()
    print(mapel)
    context = {
        'mapel': mapel
    }
    # parsing data task ke template todo/index.html dan merender nya
    return render(request, 'mapel/index.html', context)

# Membuat View untuk halaman detail task
def detail_view(request, mapel_id):
    # Mengambil data task berdasarkan task ID
    try:
        mapel = Mapel.objects.get(pk=mapel_id)
        context = {
            'mapel': mapel
        }
    except mapel.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Mapel tidak ditemukan.")
    # parsing data task ke template todo/detail.html dan merendernya
    return render(request, 'mapel/detail.html', context)

# Membuat View untuk halaman form tambah task
def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class TaskForm
        form = MapelForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = MapelForm(request.POST)
            # Simpan data ke dalam table tasks
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('mapel:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = MapelForm()
    # merender template form dengan memparsing data form
    return render(request, 'mapel/form.html', {'form': form})

# Membuat View untuk halaman form ubah task
def update_view(request, mapel_id):
    try:
        # mengambil data task yang akan diubah berdasarkan task id
        mapel = Mapel.objects.get(pk=mapel_id)
    except mapel.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Mapel tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = MapelForm(request.POST, instance=mapel)
        if form.is_valid():
            # Simpan perubahan data ke dalam table tasks
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Mengubah mapel.')
            return redirect('mapel:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = MapelForm(instance=mapel)
    # merender template form dengan memparsing data form
    return render(request, 'mapel/form.html', {'form': form})

# Membuat View untuk menghapus data task
def delete_view(request, mapel_id):
    try:
        # mengambil data task yang akan dihapus berdasarkan task id
        mapel = Mapel.objects.get(pk=mapel_id)
        # menghapus data dari table tasks
        mapel.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.success(request, 'Sukses Menghapus Mapel.')
        return redirect('mapel:index')
    except Mapel.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Mapel tidak ditemukan.")
