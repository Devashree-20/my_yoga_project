from django.contrib import admin
from .models import TimetableEntry
from .models import SessionBooking

admin.site.register(TimetableEntry)
admin.site.register(SessionBooking)