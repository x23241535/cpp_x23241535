from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm 
from .forms import UpdateAppointmentForm
from .appointmentleft import calculatetotal_remainingappointments
from cliniclib.bmiclinic_pkg.bmi import calculatebmivalue


# Create your views here.
def admin_login(request):
    return render(request, 'staff/admin_login.html')

# View for index.html
def index(request):
    appointments = Appointment.objects.all()  # Query to fetch all appointments
    context = {'appointments': appointments}
    return render(request, 'staff/index.html', context)
    
# View for mainpage
def mainpage(request):
    return render(request, 'staff/main_website.html')
    
#View for user first page
def user_firstpage(request):
    return render(request, 'staff/user_firstpage.html')
    
#View for booking appointment
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_website')  # Redirect to main_website after successful submission
    else:
        form = AppointmentForm()
    
    # Calculate remaining appointments
    remaining_appointments = calculatetotal_remainingappointments()
    
    return render(request, 'staff/user_firstpage.html', {'form': form, 'remaining_appointments': remaining_appointments})

#View for update appointment
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = UpdateAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('main_website')  # Redirect to main_website after successful update
    else:
        form = UpdateAppointmentForm(instance=appointment)
    return render(request, 'update_appointment.html', {'form': form})
    
#view for BMI
def bmiUI(request):
    bmi = None
    
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        
        bmi = calculatebmivalue(weight, height)
    
    return render(request, 'staff/bmiUI.html', {'bmi': bmi})