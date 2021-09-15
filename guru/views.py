from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404
# Create your views here.
from .models import Guru
from .forms import GuruForm
from role.models import Role
from mapel.models import Mapel

def index_view(request):
    guru = Guru.objects.all()
    context = {
        'guru' : guru
    }
    return render(request, 'guru/index.html', context)

def detail_view(request, guru_id):
    # Mengambil data task berdasarkan task ID
    try:
        guru = Guru.objects.get(pk=guru_id)
        context = {
            'guru': guru
        }
    except Guru.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Guru tidak ditemukan.")
    # parsing data task ke template todo/detail.html dan merendernya
    return render(request, 'guru/detail.html', context)

def create_view(request):
    role = Role.objects.all()
    mapel = Mapel.objects.all()
    
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class SiswaForm
        form = GuruForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = GuruForm(request.POST)
            # Simpan data ke dalam table siswa
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('guru:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = GuruForm()
        
        context = {
            'role' : role,
            'mapel': mapel,
            'form': form
        }
    # merender template form dengan memparsing data form
    return render(request, 'guru/form.html', context)

def update_view(request, guru_id):
    try:
        # mengambil data task yang akan diubah berdasarkan task id
        guru = Guru.objects.get(pk=guru_id)
    except Guru.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = GuruForm(request.POST, instance=guru)
        if form.is_valid():
            # Simpan perubahan data ke dalam table tasks
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Mengubah Guru.')
            return redirect('guru:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = GuruForm(instance=guru)
    # merender template form dengan memparsing data form
    return render(request, 'guru/form.html', {'form': form})

def delete_view(request, guru_id):
    try:
        # mengambil data task yang akan dihapus berdasarkan task id
        guru = Guru.objects.get(pk=guru_id)
        # menghapus data dari table tasks
        guru.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.success(request, 'Sukses Menghapus Guru.')
        return redirect('guru:index')
    except Guru.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    
            
            
            
    
    