from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import AppointmentData, Accept
from .admin import PatientsLogin, DoctorsLogin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import LoginHistory

@login_required
def mainPage(request):
    if request.method == 'GET':
        return render(request, 'mainpage.html')
    else:
        # Fetch credentials from POST request
        username_patient = request.POST.get('username')
        password_patient = request.POST.get('password')
        username_doctor = request.POST.get('user')
        password_doctor = request.POST.get('pass')

        # Authenticate patient user
        patient_user = authenticate(request, username=username_patient, password=password_patient)

        # Authenticate doctor user
        doctor_user = authenticate(request, username=username_doctor, password=password_doctor)

        # Determine user type and redirect
        if patient_user is not None:
            login(request, patient_user)
            return redirect(request,'patientslogin.html')
        elif doctor_user is not None:
            login(request, doctor_user)
            return redirect(request,'doctorslogin.html')
        else:
            # Authentication failed; stay on the main page with an error
            return render(request, 'mainpage.html', {'error': 'Invalid credentials'})

@login_required
def patients_login(request):
    return render(request, 'patientslogin.html')

@login_required
def doctors_login(request):
    return render(request, 'doctorslogin.html')

@login_required
def take_appointment(request):
    if request.method == 'GET':
        data = AppointmentData.objects.all()
        return render(request, 'takeappointment.html',{'data':data})
    else:
        pname1 = request.POST['pname']
        age1 = request.POST['age']
        gender1 = request.POST['gender']
        mobile1 = request.POST['mobile']
        bgroup1 = request.POST['bloodgroup']
        dname1 = request.POST['doctorsname']
        location1 = request.POST['location']
        problem1 = request.POST['problem']
        AppointmentData.objects.create(
            patients_name = pname1,
            age = age1,
            gender = gender1,
            mobile = mobile1,
            blood_group = bgroup1,
            doctors_name = dname1,
            location = location1,
            problem = problem1,
        ).save()
        data = AppointmentData.objects.all()
        return render(request, 'takeappointment.html',{'data':data})

@login_required
def check_status(request):
    data = Accept.objects.all()
    return render(request, 'checkstatus.html', {'data':data})

@login_required
def check_appointment(request):
        data = AppointmentData.objects.all()
        return render(request, 'checkappointmentpage.html',{'data':data})

@login_required
def accept(request):
    if request.method == 'GET':
        data = AppointmentData.objects.all()
        return render(request,'acceptappointment.html',{'data':data})

    else:
        date1 = request.POST['date']
        time1 = request.POST['time']
        day1 = request.POST['day']
        Accept(
        date = date1,
        time = time1,
        day = day1,
        ).save()
        data = Accept.objects.all()
        return render(request,'acceptappointment.html',{'data':data})

@login_required
def reject(request, id):
     return redirect('doctors_login')

@login_required
def my_history(request):
    login_history = LoginHistory.objects.filter(user=request.user).order_by('-login_time')
    context = {
        'login_history': login_history
    }
    return render(request, 'myhistory.html', context)

@login_required
def doctors_details(request):
    return render(request, 'doctorsdetails.html')

@login_required
def logoutpage(request):
    logout(request)
    return HttpResponse('logout here!!!')
