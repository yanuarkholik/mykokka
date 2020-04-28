from django.db import models
from django import forms
from django.utils import timezone


# Create your models here.
class Konten(models.Model):
    judul       = models.CharField(max_length=200)
    subjudul    = models.CharField(max_length=200)
    isi         = models.TextField()
    waktu       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {}'.format(self.judul, self.subjudul)

    class Meta:
        verbose_name_plural = 'Buat-Konten'

# ChoiceField
PESAN_CHOICE = [
    ('Elegant Brown', 'Elegant Brown'),
    ('Black Coil', 'Black Coil'),
    ('Combination', 'Combination'),
]

class Pesan(models.Model):
    nama        = models.CharField(max_length=100)
    email       = models.EmailField()
    telepon     = models.CharField(max_length=13)
    alamat      = models.TextField()
    kode_pos    = models.CharField(max_length=6, blank=True)
    warna       = models.CharField(max_length=20, choices=PESAN_CHOICE, default='Elegant Brown')
    jumlah      = models.IntegerField(default=0)
    date        = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Data-Pesan'

    def __str__(self):
        return '{} -- {} -- {} -- {} -- {} Warna : {} Jml : {} Date : {}'.format(self.nama, self.email, self.telepon, self.alamat, self.kode_pos, self.warna,  self.jumlah, self.date)

STOK_CHOICE = [
    ('Stok Ada', 'Stok Ada'),
    ('Stok Kosong', 'Stok Kosong'),
]

class Barang(models.Model):
    nama        = models.CharField(max_length=100)
    stok        = models.CharField(max_length=13, choices=STOK_CHOICE, default='Stok Ada')
    harga       = models.CharField(max_length=100)
    insight     = models.TextField()

    class Meta:
        verbose_name_plural = 'Buat-Barang'

    def __str__(self):
        return '{} : {}'.format(self.nama, self.stok)

class Comment(models.Model):
    nama        = models.CharField(max_length=100)
    email       = models.EmailField()
    text        = models.TextField()
    waktu       = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Data-Comment'
    
    def __str__(self):
        return '{} : {}'.format(self.nama, self.email)

class Desc(models.Model):
    sight       = models.CharField(max_length=25, null=True, blank=True)
    descr       = models.TextField()

    class Meta:
        verbose_name_plural = 'Buat-Barang-Desc'
    
    def __str__(self):
        return self.sight