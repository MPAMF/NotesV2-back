from django.contrib import admin

# Register your models here.
from .models import SessionNote, Session, SessionSelectedCourse

admin.site.register(Session)
admin.site.register(SessionNote)
admin.site.register(SessionSelectedCourse)
