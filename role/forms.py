from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Role


# membuat class TaskForm untuk membuat task
class RoleForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Role
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('name', 'descriptions')
        # mengatur teks label untuk setiap field
        labels = {
            'name': _('Daftar Nama'),
            'descriptions': _('Deskripsi'),
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'name': {
                'required': _("Judul harus diisi."),
            },
            'descriptions': {
                'required': _("Deskripsi harus diisi."),
            },
        }
