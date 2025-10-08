from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('university', 'name')

    def __str__(self):
        return f"{self.name} ({self.university.name})"


class Semester(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Örn: Güz 2024, Bahar 2025

    class Meta:
        unique_together = ('department', 'name')

    def __str__(self):
        return f"{self.name} - {self.department.name}"


class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)  # Örn: CMPE 350
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('semester', 'code')

    def __str__(self):
        return f"{self.code} - {self.name} ({self.semester.department.university.name})"


class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='notes_files/%Y/%m/%d/')
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.course.code}"