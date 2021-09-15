from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Siswa(models.Model):
    name = models.CharField(max_length=100)
    kelas = models.CharField(max_length=100)
    bidang_keahlian = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'siswa'