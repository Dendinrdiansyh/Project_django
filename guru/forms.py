from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Guru


# membuat class TaskForm untuk membuat task
class GuruForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Guru
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('name', 'usia')
        
        labels = {
            'name': _('Nama Guru'),
            'usia': _('Usia'),
        }
        
        error_messages = {
            'name': {
                'required': _("Nama Guru harus diisi."),
            },
            'usia': {
                'required': _("usia harus diisi."),
            },
        }