from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Siswa


# membuat class TaskForm untuk membuat task
class SiswaForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Siswa
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('name', 'kelas', 'bidang_keahlian')
        # mengatur teks label untuk setiap field
        labels = {
            'name': _('Daftar Nama'),
            'kelas': _('kelas'),
            'bidang_keahlian': _('bidang_keahlian')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'name': {
                'required': _("Daftar Nama harus diisi."),
            },
            'kelas': {
                'required': _("Kelas harus diisi."),
            },
        }