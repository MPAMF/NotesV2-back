from django.contrib import admin

# Register your models here.
from courses.models import Note, Course, Semester, TdGroup, TpGroup, ExamDate, Localisation, LocalisationImage

admin.site.register(Semester)
admin.site.register(TdGroup)
admin.site.register(TpGroup)
admin.site.register(Course)
admin.site.register(Note)
admin.site.register(Localisation)
admin.site.register(LocalisationImage)
admin.site.register(ExamDate)
