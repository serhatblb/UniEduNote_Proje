from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # KİMİK DOĞRULAMA (Login/Logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # KULLANICI İŞLEMLERİ (Register)
    path('accounts/', include('users.urls')),  # << YENİ EKLENDİ

    # NOT İŞLEMLERİ
    path('', include('notes.urls')),
]
# Geliştirme Ortamında Media dosyalarına erişimi açmak için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)