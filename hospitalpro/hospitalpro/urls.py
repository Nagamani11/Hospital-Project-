"""
URL configuration for hospitalpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospitalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainPage, name ='mainPage'),
    path('patients_login', views.patients_login, name = 'patients_login'),
    path('doctors_login', views.doctors_login, name = 'doctors_login'),
    path('take_appointment', views.take_appointment, name = 'take_appointment'),
    path('check_status', views.check_status, name = 'check_status'),
    path('check_appointment/', views.check_appointment, name = 'check_appointment'),
    path('accept', views.accept , name = 'accept'),
    path('reject/<int:id>/', views.reject, name='reject'),
    path('my_history', views.my_history, name = 'my_history'),
    path('doctors_details', views.doctors_details, name = 'doctors_details'),
    path('logout', views.logoutpage, name = 'logout'),
]
