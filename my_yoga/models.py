from django.db import models
from django.contrib.auth.models import User

class TimetableEntry(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    time = models.CharField(max_length=20)
    yoga_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day} - {self.time}: {self.yoga_type}"
        

class SessionBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timetable_entry = models.ForeignKey(TimetableEntry, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Booking for {self.full_name} on {self.timetable_entry.day} at {self.timetable_entry.time}"