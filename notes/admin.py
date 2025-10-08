from django.contrib import admin
# Semester modelini buraya ekledik!
from .models import University, Department, Semester, Course, Note

# Oluşturduğumuz tüm modelleri Admin paneline kaydettik.
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Semester) # Yeni model
admin.site.register(Course)
admin.site.register(Note)