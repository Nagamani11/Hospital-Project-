from django.db import models
from django.contrib.auth.models import User

class PatientsLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class DoctorsLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class AppointmentData(models.Model):
    patients_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    blood_group = models.CharField(max_length=50)
    doctors_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    problem = models.CharField(max_length=50)

class Accept(models.Model):
    date = models.DateField()
    time = models.TimeField()
    day = models.CharField(max_length=50)


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} logged in at {self.login_time}"
