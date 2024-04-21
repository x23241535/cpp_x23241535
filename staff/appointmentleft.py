from .models import Appointment

# Function for  calculating remaining appointments
def calculatetotal_remainingappointments():
    totalnumberof_appointments = 20
    currentnumberof_appointments = Appointment.objects.count()
    remainingnumberof_appointments = totalnumberof_appointments - currentnumberof_appointments
    return remainingnumberof_appointments

def remainingnumberof_appointments_context_processor(request):
    remainingnumberof_appointments = calculatetotal_remainingappointments()
    return {'remainingnumberof_appointments': remainingnumberof_appointments}