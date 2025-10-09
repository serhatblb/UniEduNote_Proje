# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # Login kontrolü için
from django.contrib import messages
from .forms import CustomUserCreationForm

# KAYIT GÖRÜNÜMÜ
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Hesabınız başarıyla oluşturuldu!")
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    context = {'form': form, 'title': 'Kayıt Ol'}
    # Bu template yolu artık registration klasöründe olacak (Aşağıda tanımlanacak)
    return render(request, 'users/register.html', context)

@login_required
def profile_view(request):
    # Hesap bilgilerini göstermek için context'i hazırlıyoruz
    context = {
        'title': 'Hesap Bilgileri',
        'user_notes_count': request.user.note_set.count(), # Yüklediği not sayısını da gösterelim
        'user': request.user
        # İleride buraya formlar eklenecek (Parola değiştirme, Bilgi güncelleme)
    }
    return render(request, 'users/profile.html', context)