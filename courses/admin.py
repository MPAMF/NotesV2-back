from django.contrib import admin

# Register your models here.
from courses.models import Note, Course, Semester, Degree, ExamDate, \
    Localisation, LocalisationImage


class CourseAdmin(admin.ModelAdmin):
    ordering = ('semester',)


class NoteAdmin(admin.ModelAdmin):
    ordering = ('course',)


admin.site.register(Semester)
admin.site.register(Degree)
admin.site.register(Course, CourseAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Localisation)
admin.site.register(LocalisationImage)
admin.site.register(ExamDate)
