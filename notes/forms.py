from django import forms
from .models import Note, Course, Semester, Department, University


class NoteUploadForm(forms.ModelForm):
    # YENİ EKLENEN FİLTRE ALANLARI (Bunlar Note modeline KAYDEDİLMEZ, sadece seçim için var)
    university = forms.ModelChoiceField(
        queryset=University.objects.all(),
        label="1. Üniversiteyi Seçin",
        required=False,  # Zorunlu değil, çünkü bu alan filtreleme için
        empty_label="--- Üniversite Seçin ---",
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_university'})
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.none(),  # Başlangıçta boş
        label="2. Bölümü Seçin",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_department'})
    )

    semester = forms.ModelChoiceField(
        queryset=Semester.objects.none(),  # Başlangıçta boş
        label="3. Dönemi Seçin",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_semester'})
    )

    # Note modeline ait asıl alanlar
    class Meta:
        model = Note
        # Formda görünmesini istediğimiz alanlar:
        fields = ['title', 'description', 'course', 'file']

        # Alanların tarayıcıda nasıl görüneceğini güzelleştirelim (Bootstrap için)
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Not başlığı (Örn: Vize Konuları Özeti)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,
                                                 'placeholder': 'Notun içeriği, hangi konuları kapsadığı vb.'}),
            'course': forms.Select(attrs={'class': 'form-select', 'id': 'id_course'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Başlangıçta ders listesini temiz ve basit tutalım
        self.fields['course'].queryset = Course.objects.none()

        # Eğer formda bir üniversite seçilmişse, ilgili bölümleri yükle
        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass  # Hata olursa varsayılan boş kalsın

        # İPUCU: Dinamik filtreleme JavaScript/AJAX ile yapılacaktır.
        # Şu an formda tüm alanlar görünecek ancak filtreleme çalışmayacaktır.
        class NoteFilterForm(forms.Form):
            # Bu form, sadece filtreleme yapmak için kullanılır, Model ile bağlantısı yoktur.

            university = forms.ModelChoiceField(
                queryset=University.objects.all().order_by('name'),
                label="Üniversite",
                required=False,
                empty_label="Tüm Üniversiteler",
                widget=forms.Select(attrs={'class': 'form-select', 'id': 'filter_university'})
            )

            department = forms.ModelChoiceField(
                queryset=Department.objects.none(),
                label="Bölüm",
                required=False,
                empty_label="Tüm Bölümler",
                widget=forms.Select(attrs={'class': 'form-select', 'id': 'filter_department'})
            )

            semester = forms.ModelChoiceField(
                queryset=Semester.objects.none(),
                label="Dönem",
                required=False,
                empty_label="Tüm Dönemler",
                widget=forms.Select(attrs={'class': 'form-select', 'id': 'filter_semester'})
            )

            # Not: Arama çubuğu (başlık/ders kodu) için ekstra bir alan şimdilik eklemeye gerek yok,
            # onu direk GET parametresi olarak alabiliriz.


class NoteFilterForm(forms.Form):
    # Bu form, sadece filtreleme yapmak için kullanılır, Model ile bağlantısı yoktur.

    university = forms.ModelChoiceField(
        queryset=University.objects.all().order_by('name'),
        label="Üniversite",
        required=False,
        empty_label="Tüm Üniversiteler",
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'filter_university'})
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.none(),
        label="Bölüm",
        required=False,
        empty_label="Tüm Bölümler",
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'filter_department'})
    )

    semester = forms.ModelChoiceField(
        queryset=Semester.objects.none(),
        label="Dönem",
        required=False,
        empty_label="Tüm Dönemler",
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'filter_semester'})
    )

    # Not: Arama çubuğu (başlık/ders kodu) için ekstra bir alan şimdilik eklemeye gerek yok,
    # onu direk GET parametresi olarak alabiliriz.