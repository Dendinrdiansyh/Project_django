from django.db import models

# Create your models here.
class Guru(models.Model):
    name = models.CharField(max_length=100)
    usia = models.CharField(max_length=100)
    mapel = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'guru'