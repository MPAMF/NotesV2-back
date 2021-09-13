from django.contrib import admin

# Register your models here.
from sessions.models import SessionNote, Session

admin.site.register(Session)
admin.site.register(SessionNote)
