from django.utils.translation import gettext_lazy as _
from django.db import models

class Data(models.Model):
    # define status choices/options
    class DataStatus(models.TextChoices):
        Aktif = 'Aktif', _('Aktif')
        Calon = 'Calon', _('Calon')
        Tidak_Aktif = 'Tidak Aktif', _('Tidak Aktif')
        Mantan = 'Mantan', _('Mantan')
    class AsistenStatus(models.TextChoices):
        Praktikum = 'Praktikum', _('Praktikum')
        Riset = 'Riset', _('Riset')
    
    # define columns
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=100)
    kelas = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    status_asisten = models.CharField(
        max_length=20,
        choices=AsistenStatus.choices,
        default=AsistenStatus.Praktikum
    )    
    
    status_data = models.CharField(
        max_length=20,
        choices=DataStatus.choices,
        default=DataStatus.Aktif
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # define table name
        db_table = 'data'