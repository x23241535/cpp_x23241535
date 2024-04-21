from django import forms
from staff.models import Appointment

#Form for Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'appointment_day']
        

#Form for Update Appointment
class UpdateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'appointment_day']