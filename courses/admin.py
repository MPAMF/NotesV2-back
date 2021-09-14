from django.contrib import admin

# Register your models here.
from courses.models import Note, Course

admin.site.register(Course)
admin.site.register(Note)
