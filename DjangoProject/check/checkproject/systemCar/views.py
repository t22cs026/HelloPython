from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.http import HttpResponse , request

# Create your views here.

class EmployeeLoginView(LoginView):
    def get_success_url(self):
        return self.request.GET.get('next') or '/systemCar/carender/'
    
class CarenderView(TemplateView):
    template_name = 'systemCar/carender.html'
    
class ReportHistory(TemplateView):
    template_name='systemCar/reporthistory.html'
    
class ReportToPDF(TemplateView):
    template_name='systemCar/reportToPDF.html'
    
    