from django.urls import path

#import view-view dari mendata/views.py
from .views import index_view, detail_view, create_view, update_view, delete_view
app_name = 'mendata'
urlpatterns = [
    # url untuk halaman daftar table data
    path('', index_view, name='index'),
    # url untuk halaman detail 
    path('<int:data_id>', detail_view, name='detail'),
    # url untuk halaman tambah data
    path('create', create_view, name='create'),
     # url untuk halaman ubah data
    path('update/<int:data_id>', update_view, name='update'),
    # url untuk menghapus data
    path('delete/<int:data_id>', delete_view, name='delete'),
]