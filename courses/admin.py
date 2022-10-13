from django.contrib import admin

# Register your models here.
from courses.models import Note, Course, Semester, Degree, ExamDate, \
    Localisation, LocalisationImage


class CourseAdmin(admin.ModelAdmin):
    ordering = ('semester',)
    search_fields = ['semester__degree__name']


class NoteAdmin(admin.ModelAdmin):
    ordering = ('course',)
    search_fields = ['course__semester__degree__name']


admin.site.register(Semester)
admin.site.register(Degree)
admin.site.register(Course, CourseAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Localisation)
admin.site.register(LocalisationImage)
admin.site.register(ExamDate)
