from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Data dari file mendata/models.py
from .models import Data

# membuat class DataForm untuk membuat data baru
class DataForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Data
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('nama', 'nim', 'kelas', 'jurusan', 'status_asisten', 'status_data')
        # mengatur teks label untuk setiap field
        labels = {
            'nama': _('Nama'),
            'nim': _('NIM'),
            'kelas': _('Kelas'),
            'jurusan': _('Jurusan'),
            'status_asisten': _('Status Asisten'),
            'status_data': _('Status Keaktifan')
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'nama': {
                'required': _("Nama harus diisi."),
            },
            'nim': {
                'required': _("NIM harus diisi."),
            },
            'kelas': {
                'required': _("Kelas harus diisi."),
            },
            'jurusan': {
                'required': _("Jurusan harus diisi."),
            },
        }
