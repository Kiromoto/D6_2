from django.shortcuts import render, reverse, redirect
from django.views import View
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appointment


class AppointmentView(LoginRequiredMixin, View):
    model = Appointment
    template_name = 'make_appointment.html'
    context_object_name = 'appointment'

    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(date=datetime.strptime(request.POST['date'], '%Y-%M-%d'),
                                  client_name=request.POST['client_name'],
                                  message=request.POST['message'],)
        appointment.save()
        return redirect('make_appointment')

