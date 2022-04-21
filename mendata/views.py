from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib import messages
# import class Data dari file mendata/models.py
from .models import Data
# import class DataForm dari file mendata/forms.py
from .forms import DataForm

# Membuat View untuk halaman daftar tabel data
def index_view(request):
    # Mengambil semua data dari class "Data" pada models.py
    semua_data = Data.objects.all()
    # Mendefinisikan nilai balik hasil request dari 'semua_data' ke 'datas' 
    # yang akan digunakan pada index.html
    context = {
        'datas': semua_data
    }
    # memparsing data ke template mendata/index.html dan merender nya
    return render(request, 'mendata/index.html', context)

# Membuat View untuk halaman detail 
def detail_view(request, data_id):
# Mengambil data berdasarkan ID
    try:
        # Mengambil data berdasarkan ID dari class "Data" pada models.py
        detail = Data.objects.get(pk=data_id)
        # Mendefinisikan nilai balik hasil request dari 'detail' ke 'data' 
        # yang akan digunakan pada index.html, dan form.html
        context = {
            'data': detail
        }
    except Data.DoesNotExist:
        # Jika data tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Data tidak ditemukan.")
    # parsing data ke template mendata/detail.html dan merendernya
    return render(request, 'mendata/detail.html', context)

# View untuk tambah data
def create_view(request):
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        # membuat objek dari class DataForm
        form = DataForm(request.POST)
        # Mengecek validasi form
        if form.is_valid():
            # Membuat Data baru dengan data yang disubmit
            new_data = DataForm(request.POST)
            # Simpan data ke dalam table 
            new_data.save()
            # mengeset pesan sukses dan redirect ke halaman view table
            messages.success(request, 'Sukses Menambah Data baru.')
            return redirect('mendata:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class DataForm
        form = DataForm()
    # merender template form dengan memparsing data form, agar terbaca pada form.html
    return render(request, 'mendata/form.html', {'form': form})

# Membuat View untuk halaman form ubah data
def update_view(request, data_id):
    try:
        # mengambil data yang akan diubah berdasarkan id
        ubah = Data.objects.get(pk=data_id)
    except Data.DoesNotExist:
        # Jika data tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Data tidak ditemukan.")
    # Mengecek method pada request
    # Jika method-nya adalah POST, maka akan dijalankan
    # proses validasi dan penyimpanan data
    if request.method == 'POST':
        form = DataForm(request.POST, instance=ubah)
        if form.is_valid():
            # Simpan perubahan data ke dalam table 
            form.save()
            # mengeset pesan sukses dan redirect ke halaman daftar table
            messages.success(request, 'Sukses Mengubah Data.')
            return redirect('mendata:index')
    # Jika method-nya bukan POST
    else:
        # membuat objek dari class DataForm
        form = DataForm(instance=ubah)
    # merender template form dengan memparsing data form, agar terbaca pada form.html
    return render(request, 'mendata/form.html', {'form': form})

# Membuat View untuk menghapus data 
def delete_view(request, data_id):
    try:
        # mengambil data data_lama yang akan dihapus berdasarkan id
        data_lama = Data.objects.get(pk=data_id)
        # menghapus data dari table 
        data_lama.delete()
        # mengeset pesan sukses dan redirect ke halaman daftar table
        messages.success(request, 'Sukses Menghapus Data.')
        return redirect('mendata:index')
    except Data.DoesNotExist:
        # Jika data tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Data tidak ditemukan.")