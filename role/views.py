from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponse
from .models import Role
from .forms import RoleForm
def index_view(request):
    role = Role.objects.all()
    context = {
        'no' : 1,
        'role': role
    }
    # memparsing data task ke template todo/index.html dan merender nya
    return render(request, 'role/index.html', context)

# Membuat View untuk halaman detail task
def detail_view(request, role_id):
    # Mengambil data task berdasarkan task ID
    try:
        role = Role.objects.get(pk=role_id)
        context = {
            'role': role
        }
    except Role.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # parsing data task ke template todo/detail.html dan merendernya
    return render(request, 'role/detail.html', context)

def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class TaskForm
        form = RoleForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Task baru dengan data yang disubmit
            new_task = RoleForm(request.POST)
            # Simpan data ke dalam table tasks
            new_task.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Menambah ROLE baru.')
            return redirect('role')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = RoleForm()
    # merender template form dengan memparsing data form
    return render(request, 'role/form.html', {'form': form})

def update_view(request, role_id):
    try:
        # mengambil data task yang akan diubah berdasarkan task id
        role = Role.objects.get(pk=role_id)
    except role.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            # Simpan perubahan data ke dalam table tasks
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar task
            messages.success(request, 'Sukses Mengubah Task Role.')
            return redirect('role')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class TaskForm
        form = RoleForm(instance=role)
    # merender template form dengan memparsing data form
    return render(request, 'role/form.html', {'form': form})

def delete_view(request, role_id):
    try:
        # mengambil data task yang akan dihapus berdasarkan task id
        role = Role.objects.get(pk=role_id)
        # menghapus data dari table tasks
        role.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar task
        messages.success(request, 'Sukses Menghapus Task.')
        return redirect('role')
    except Role.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")