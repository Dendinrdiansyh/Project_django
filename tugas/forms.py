from django.forms import ModelForm
from .models import Tugas

class TugasForm(ModelForm):
    class Meta:
        model = Tugas
        fields = '__all__'