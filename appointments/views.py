from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment
from django.utils.decorators import method_decorator
from django import views
# Create your views here.
# @login_required
# def appointment_list(request):
#     appoinments = Appointment.objects.all()
#     return render(request, 'app_list.html', {'appointments': appoinments})

class AppointmentListView(views.View):

    def get(self, request):
        appoinments = Appointment.objects.all()
        return render(request, 'app_list.html', {'appointments': appoinments})

    def post(self, request):
        pass


