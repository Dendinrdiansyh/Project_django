from django.shortcuts import redirect,render
from django.http import Http404
 
# Create your views here.
from django.http import HttpResponse

# import class Task dari file todo/models.py
from .models import Siswa
# import class TaskForm dari file todo/forms.py
from .forms import SiswaForm
from role.models import Role

# Membuat View untuk halaman daftar task
def index_view(request):
    # Mengambil semua data task
    siswa = Siswa.objects.all()
    context = {
        'siswa': siswa
    }
    # memparsing data task ke template todo/index.html dan merender nya
    return render(request, 'siswa/index.html', context)

# Membuat View untuk halaman detail siswa
def detail_view(request, siswa_id):
    # Mengambil data task berdasarkan siswa ID
    try:
        siswa = Siswa.objects.get(pk=siswa_id)
        context = {
            'siswa': siswa
        }
    except Siswa.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Siswa tidak ditemukan.")
    # parsing data task ke template todo/detail.html dan merendernya
    return render(request, 'siswa/detail.html', context)

# Membuat View untuk halaman form tambah siswa
def create_view(request):
    role = Role.objects.all()
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        
        # membuat objek dari class SiswaForm
        form = SiswaForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = SiswaForm(request.POST)
            # Simpan data ke dalam table siswa
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('siswa:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = SiswaForm()
        context = {
            'role':role,
            'form': form
        }
        
    # merender template form dengan memparsing data form
    return render(request, 'siswa/form.html', context)

# Membuat View untuk halaman form ubah task
def update_view(request, siswa_id):
    try:
        # mengambil data task yang akan diubah berdasarkan task id
        siswa = Siswa.objects.get(pk=siswa_id)
    except Siswa.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Siswa tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = SiswaForm(request.POST, instance=siswa)
        if form.is_valid():
            # Simpan perubahan data ke dalam table tasks
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Mengubah Task.')
            return redirect('siswa:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = SiswaForm(instance=siswa)
    # merender template form dengan memparsing data form
    return render(request, 'siswa/form.html', {'form': form})

# Membuat View untuk menghapus data task
def delete_view(request, siswa_id):
    try:
        # mengambil data task yang akan dihapus berdasarkan task id
        siswa = Siswa.objects.get(pk=siswa_id)
        # menghapus data dari table tasks
        siswa.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.success(request, 'Sukses Menghapus Siswa.')
        return redirect('siswa:index')
    except Siswa.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Siswa tidak ditemukan.")
