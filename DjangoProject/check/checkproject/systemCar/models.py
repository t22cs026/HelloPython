from django.db import models

# Create your models here.

class Employee(models.Model):
    employeeID = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return '{}({})'.format(self.name,self.employeeID)
    
class DailyReport(models.Model):
    user = Employee
    departure_date = models.DateField
    return_date = models.DateField
    checker = models.CharField(max_length=100)        
    reportID = models.PositiveIntegerField(default=0)