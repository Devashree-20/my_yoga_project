from django import forms
from .models import SessionBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = SessionBooking
        fields = ['full_name', 'email', 'phone', 'additional_notes']
