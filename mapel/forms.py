from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Mapel


# membuat class TaskForm untuk membuat task
class MapelForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Mapel
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('nama_guru', 'pelajaran', 'jam_pelajaran')
        # mengatur teks label untuk setiap field
        labels = {
            'nama_guru': _('judul'),
            'pelajaran': _('Deskripsi'),
            'jam_pelajaran': _('Status')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'nama_guru': {
                'required': _("Judul harus diisi."),
            },
            'pelajaran': {
                'required': _("Deskripsi harus diisi."),
            },
        }