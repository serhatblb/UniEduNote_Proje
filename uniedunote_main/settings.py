from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!!)u=h9!cyf_eips%#8&o(yp5dw9iy5=zb28+ldb&qe*-is0-6'
DEBUG = True
ALLOWED_HOSTS = []

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
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
        # Burada ana templates klasörünü ekledik 👇
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
STATICFILES_DIRS = [BASE_DIR / 'static']  # (Eğer static klasörün varsa)

# === MEDIA FILES (Eğer dosya yükleme yapıyorsan) ===
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# === DEFAULT PRIMARY KEY FIELD TYPE ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === LOGIN / LOGOUT AYARLARI ===
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'home'
