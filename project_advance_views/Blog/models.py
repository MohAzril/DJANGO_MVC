from django.db import models
from django.utils import timezone

class Blog(models.Model):
    nama = models.CharField(max_length=255)
    gambar = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    deskripsi = models.TextField(max_length=500)

    def __str__(self):
        return self.nama
# Create your models here.
