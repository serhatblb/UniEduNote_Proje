# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model  # 🚨 YENİ İMPORT

# CustomUser'ı bu şekilde import ETME:
# from .models import CustomUser

# get_user_model() ile kullanıcı modelini dinamik olarak al
CustomUser = get_user_model()  # 🚨 CustomUser'ı bu şekilde tanımlıyoruz!


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-posta Adresi")

    # Eğer first_name ve last_name zorunlu olsun istiyorsan bunları da ekle:
    # first_name = forms.CharField(required=True, label="Ad")
    # last_name = forms.CharField(required=True, label="Soyad")

    class Meta(UserCreationForm.Meta):
        # Artık model=CustomUser hatasız çalışacak
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

# ...