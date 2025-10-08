from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('upload/', views.upload_note, name='upload_note'),

    # Not Listeleme ve Detay
    path('notes/', views.note_list_view, name='note_list'),
    path('notes/<int:pk>/', views.note_detail_view, name='note_detail'),
    path('notes/<int:pk>/download/', views.download_note, name='download_note'),
    path('notes/<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('notes/<int:pk>/edit/', views.edit_note, name='edit_note'),

    # AJAX Adresleri (Yükleme ve Filtreleme için Ortak)
    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'),
    path('ajax/load-semesters/', views.load_semesters, name='ajax_load_semesters'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
]