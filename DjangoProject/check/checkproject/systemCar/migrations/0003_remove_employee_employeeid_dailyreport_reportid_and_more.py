# Generated by Django 4.1.7 on 2024-11-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("systemCar", "0002_dailyreport"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="employeeId",
        ),
        migrations.AddField(
            model_name="dailyreport",
            name="reportID",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="employee",
            name="employeeID",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
