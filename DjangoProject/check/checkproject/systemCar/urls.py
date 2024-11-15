from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
     path('login/' , views.EmployeeLoginView.as_view(template_name='systemCar/login.html'),name="login"),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('carender/',views.CarenderView.as_view(),name="carender"),
     path('report/history/',views.ReportHistory.as_view(),name='reporthistory'),
     path('report/topdf/',views.ReportToPDF.as_view(),name='toPDF'),
]
