from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

class Mapel(models.Model):
    nama_guru = models.CharField(max_length=50)
    pelajaran = models.CharField(max_length=20)
    jam_pelajaran = models.CharField(max_length=20)
    
    
    
    class Meta:
        # define table name
        db_table = 'mapel'