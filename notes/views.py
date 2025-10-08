from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Note, Department, Semester, Course, University
from .forms import NoteUploadForm, NoteFilterForm
from django.http import JsonResponse, FileResponse # FileResponse'u ekle
import os #
from django.contrib import messages
def home_page(request):
    return render(request, 'notes/home.html')


@login_required  # Sadece giriş yapan kullanıcılar indirebilir
def download_note(request, pk):
    # 1. Not nesnesini al
    note = get_object_or_404(Note, pk=pk)

    # 2. Dosya yolunu al (Django'nun FileField özelliği ile)
    file_path = note.file.path

    # 3. Dosyanın sunucuda varlığını kontrol et (olası hatalara karşı)
    if not os.path.exists(file_path):
        # Dosya bulunamazsa notun detay sayfasına yönlendirilebilir
        messages.error(request, "İndirilmeye çalışılan dosya bulunamadı.")
        return redirect('note_detail', pk=pk)

        # 4. FileResponse ile dosyayı güvenli bir şekilde gönder
    # as_attachment=True: Tarayıcıya dosyayı indirmesini söyler
    # filename: Kullanıcının göreceği dosya adını belirler
    response = FileResponse(
        open(file_path, 'rb'),  # Dosyayı binary (ikilik) modda aç
        as_attachment=True,
        filename=os.path.basename(file_path)  # Dosya adını kullan
    )

    return response
@login_required
def dashboard_view(request):
    return render(request, 'notes/dashboard.html')


@login_required
def upload_note(request):
    form = NoteUploadForm(request.POST or None, request.FILES or None)

    # AJAX'tan gelen üniversite/bölüm seçimlerini işleyerek diğer dropdown'ları doldur
    if 'university' in request.POST:
        try:
            university_id = int(request.POST.get('university'))
            form.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
        except (ValueError, TypeError):
            pass

    if 'department' in request.POST:
        try:
            department_id = int(request.POST.get('department'))
            form.fields['semester'].queryset = Semester.objects.filter(department_id=department_id).order_by('name')
        except (ValueError, TypeError):
            pass

    if 'semester' in request.POST:
        try:
            semester_id = int(request.POST.get('semester'))
            form.fields['course'].queryset = Course.objects.filter(semester_id=semester_id).order_by('code')
        except (ValueError, TypeError):
            pass

            # Form kaydedilirse
    if form.is_valid():
        note = form.save(commit=False)
        note.uploader = request.user
        note.save()
        return redirect('dashboard')  # Başarılı yüklemeden sonra dashboard'a yönlendir

    context = {'form': form}
    return render(request, 'notes/upload_note.html', context)


# --- NOT LİSTELEME VE FİLTRELEME GÖRÜNÜMÜ ---
def note_list_view(request):
    form = NoteFilterForm(request.GET)
    notes_queryset = Note.objects.all().select_related(
        'course__semester__department__university',
        'uploader'
    ).order_by('-upload_date')

    # 2. AJAX ile Filtreleme Formu alanlarını doldur
    if 'university' in request.GET:
        try:
            uni_id = int(request.GET.get('university'))
            form.fields['department'].queryset = Department.objects.filter(university_id=uni_id).order_by('name')
        except (ValueError, TypeError):
            pass

    if 'department' in request.GET:
        try:
            dept_id = int(request.GET.get('department'))
            form.fields['semester'].queryset = Semester.objects.filter(department_id=dept_id).order_by('name')
        except (ValueError, TypeError):
            pass

            # 3. QuerySet'i Filtrele
    filters = {}
    if request.GET.get('university'):
        filters['course__semester__department__university__id'] = request.GET.get('university')

    if request.GET.get('department'):
        filters['course__semester__department__id'] = request.GET.get('department')

    if request.GET.get('semester'):
        filters['course__semester__id'] = request.GET.get('semester')

    search_query = request.GET.get('q')
    if search_query:
        notes_queryset = notes_queryset.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(course__code__icontains=search_query)
        )

    if filters:
        notes_queryset = notes_queryset.filter(**filters)

    context = {
        'notes': notes_queryset,
        'note_count': notes_queryset.count(),
        'title': 'Tüm Notları Keşfet',
        'filter_form': form,
        'current_search_query': search_query or ''
    }
    return render(request, 'notes/note_list.html', context)


# --- NOT DETAY GÖRÜNÜMÜ ---
def note_detail_view(request, pk):
    note = get_object_or_404(
        Note.objects.select_related('course__semester__department__university', 'uploader'),
        pk=pk
    )
    context = {
        'note': note,
        'title': note.title
    }
    return render(request, 'notes/note_detail.html', context)


# --- AJAX FONKSİYONLARI ---
def load_departments(request):
    university_id = request.GET.get('university_id')
    departments = Department.objects.filter(university_id=university_id).order_by('name')
    department_list = [{'id': department.id, 'name': department.name} for department in departments]
    return JsonResponse(department_list, safe=False)


def load_semesters(request):
    department_id = request.GET.get('department_id')
    semesters = Semester.objects.filter(department_id=department_id).order_by('name')
    semester_list = [{'id': semester.id, 'name': semester.name} for semester in semesters]
    return JsonResponse(semester_list, safe=False)


def load_courses(request):
    semester_id = request.GET.get('semester_id')
    courses = Course.objects.filter(semester_id=semester_id).order_by('code')
    course_list = [{'id': course.id, 'name': f"{course.code} - {course.name}"} for course in courses]
    return JsonResponse(course_list, safe=False)