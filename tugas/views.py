from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.http import HttpResponse
# import class Task dari file todo/models.py
from .models import Tugas
from siswa.models import Siswa
from mapel.models import Mapel
from todo.models import Todo
# import class TaskForm dari file todo/forms.py
from .forms import TugasForm

# Membuat View untuk halaman daftar task
def index_view(request):
    # Mengambil semua data task
    tugas = Tugas.objects.all()
    context = {
        'tugas': tugas
    }
    # parsing data task ke template todo/index.html dan merender nya
    return render(request, 'tugas/index.html', context)

# Membuat View untuk halaman form tambah task
def create_view(request):
    
    siswa = Siswa.objects.all()
    mapel = Mapel.objects.all()
    todo = Todo.objects.all()
    
    context = {
        'mapel': mapel,
        'siswa': siswa,
        'todo' : todo
    }
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        Tugas.objects.create(
            nama_siswa  = request.POST['nama_siswa'],
            mata_pelajaran = request.POST['pelajaran'],
            tugas      = request.POST['tugas'],
        )
        
            # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.success(request, 'Sukses Menambah Task baru.')
        return redirect('index')
    # Jika method-nya bukan POST
    else:
    # merender template form dengan memparsing data form
        return render(request, 'tugas/form.html', context)

# Membuat View untuk halaman form ubah task
def update_view(request, tugas_id):
    try:
        # mengambil data task yang akan diubah berdasarkan task id
        tugas = Tugas.objects.get(pk=tugas_id)
    except Tugas.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = TugasForm(request.POST, instance=tugas)
        if form.is_valid():
            # Simpan perubahan data ke dalam table tasks
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Mengubah Task.')
            return redirect('tugas:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = TugasForm(instance=tugas)
    # merender template form dengan memparsing data form
    return render(request, 'tugas/form.html', {'form': form})

# Membuat View untuk menghapus data task
def delete_view(request, tugas_id):
    try:
        # mengambil data task yang akan dihapus berdasarkan task id
        tugas = Tugas.objects.get(pk=tugas_id)
        # menghapus data dari table tasks
        tugas.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.success(request, 'Sukses Menghapus Task.')
        return redirect('index')
    except Tugas.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Tugas tidak ditemukan.")