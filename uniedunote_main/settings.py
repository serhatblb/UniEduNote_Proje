from pathlib import Path
import os # os modülünü ekledik!

BASE_DIR = Path(__file__).resolve().parent.parent

# 🚨 GÜVENLİK AYARLARI 🚨

# SECRET_KEY'i gizli tutmalısın. Üretimde bu değer ortam değişkenlerinden gelmeli!
SECRET_KEY = 'django-insecure-!!)u=h9!cyf_eips%#8&o(yp5dw9iy5=zb28+ldb&qe*-is0-6'

# 1. KRİTİK: Güvenlik için False yapıldı!
DEBUG = False

# 2. KRİTİK: Uygulamanın çalışacağı domain'leri buraya ekle.
# Yayınladığında: 'myuniedunote.com', 'www.myuniedunote.com' gibi olmalı.
# Şimdilik '*' ile tüm host'lara izin verebiliriz (Test amaçlı).
ALLOWED_HOSTS = ['*'] # YAYINDA GÜVENLİK İÇİN LÜTFEN ASIL DOMAIN'İ YAZ!
if 'RENDER_EXTERNAL_HOSTNAME' in os.environ:
    ALLOWED_HOSTS.append(os.environ['RENDER_EXTERNAL_HOSTNAME'])

# === APPS ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes',
    'users',
    'widget_tweaks',
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Diğer middleware'ler...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uniedunote_main.urls'

# === TEMPLATES ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'uniedunote_main.wsgi.application'

# === DATABASE ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === PASSWORD VALIDATION ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === INTERNATIONALIZATION ===
LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

# === STATIC FILES ===
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 3. KRİTİK: Üretim ortamında statik dosyaların toplanacağı yer.
# `python manage.py collectstatic` çalıştırıldığında bu klasör oluşur.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# === MEDIA FILES (Yüklenen dosyalar) ===
MEDIA_URL = '/media/'
# os.path.join kullanıldı, Path yerine (daha geniş uyumluluk için)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# === DEFAULT PRIMARY KEY FIELD TYPE ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === LOGIN / LOGOUT AYARLARI ===
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'home'

# E-POSTA AYARLARI (Parola sıfırlama için)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'support@uniedunote.com'