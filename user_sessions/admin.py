from django.contrib import admin

# Register your models here.
from .models import SessionNote, Session

admin.site.register(Session)
admin.site.register(SessionNote)
