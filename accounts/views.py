from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile


def home(request):
    return render(request, 'accounts/home.html')


def register_view(request):

    error = None

    if request.method == 'POST':

        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        account_type = request.POST.get('account_type', 'tourist')
        terms = request.POST.get('terms')

        if not full_name or not email or not password or not confirm_password:
            error = "Please complete all required fields."

        elif not terms:
            error = "Please accept the terms before creating your account."

        elif len(full_name) < 2:
            error = "Please enter your full name."

        elif password != confirm_password:
            error = "The passwords do not match."

        elif len(password) < 8:
            error = "Your password must contain at least 8 characters."

        elif not any(char.isdigit() for char in password):
            error = "Your password must contain at least one number."

        elif account_type not in ['tourist', 'guide']:
            error = "Please select a valid account type."

        elif User.objects.filter(username=email).exists():
            error = "An account with this email already exists. Please log in."

        else:

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name
            )

            Profile.objects.create(
                user=user,
                role=account_type
            )

            return redirect('/accounts/login/')

    return render(
        request,
        'accounts/register.html',
        {
            'error': error,
        }
    )


def login_view(request):

    error = None

    if request.method == 'POST':

        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        if not email or not password:

            error = "Please enter your email address and password."

        else:

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:

                login(request, user)

                if hasattr(user, 'profile'):

                    if user.profile.role == 'guide':
                        return redirect('/guide/')

                    return redirect('/tourist/')

                error = "Your account profile could not be found."

            else:

                error = "The email or password is incorrect."

    return render(
        request,
        'accounts/login.html',
        {
            'error': error,
        }
    )