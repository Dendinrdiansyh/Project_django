from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Tugas(models.Model):
    nama_siswa = models.CharField(max_length=100)
    mata_pelajaran = models.CharField(max_length=100)
    tugas = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'tugas'