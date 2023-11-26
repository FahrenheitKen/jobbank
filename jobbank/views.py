from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Userprofile
from .models import EmployerProfile


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def jobs(request):
    return render(request, 'job-list.html')


def contacts(request):
    return render(request, 'contact.html')


def error(request):
    return render(request, '404.html')


def login_signup(request):
    return render(request, 'login_signup.html')


def Job_seeker_signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['signup-email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = User.objects.create_user(username=email, email=email, password=password, )
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        Userprofile.objects.create(user=user, phone_number=phone_number)

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('job_seeker_signup')

    elif 'login_email' in request.POST:
        email = request.POST['login_email']
        password = request.POST['login_password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('job_seeker_signup')

    return render(request, 'Jobseeker.html')


def employer_signup(request):
    if request.method == 'POST':
        business_name = request.POST['business_name']
        phone_number = request.POST['employer_phone_number']
        email = request.POST['employer_email']
        password = request.POST['employer_password']

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        EmployerProfile.objects.create(user=user, buiness_name=business_name, phone_number=phone_number)

        user = authenticate(request, username=email, password=password)
        if user is None:
            login(request, user)
            return redirect('employer_signup')

    elif 'employer_email' in request.POST:
        email = request.POST['employer_email']
        password = request.POST['login_password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('employer_signup')

    return render(request, 'employer.html')
