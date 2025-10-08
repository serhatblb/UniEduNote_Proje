# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # Kayıt formunda kullanıcı adı ve e-posta alalım
        fields = ('username', 'email')