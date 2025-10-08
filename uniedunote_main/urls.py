from django.contrib import admin
from django.urls import path, include # 'include' kelimesini ekledik

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Yeni eklenen satır: Uygulamamızın (notes) adreslerini buraya dahil ediyoruz.
    path('', include('notes.urls')),
]