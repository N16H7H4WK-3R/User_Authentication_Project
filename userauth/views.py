from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            messages.success(request, 'Logged in successfully!')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'auth/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password1)
            messages.success(
                request, 'Account created successfully! Please log in.')
            return redirect('login')
    return render(request, 'auth/signup.html')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, 'Please enter your email address.')
        elif not User.objects.filter(email=email).exists():
            messages.error(request, 'No account found with this email address.')
        else:
            try:
                form = PasswordResetForm({'email': email})
                if form.is_valid():
                    form.save(
                        request=request,
                        from_email=None,
                        email_template_name='auth/password_reset_email.html',
                        subject_template_name='auth/password_reset_subject.txt'
                    )
                    messages.success(request, 'Password reset instructions sent to your email.')
                    return redirect('password_reset_done')
                else:
                    for field, errors in form.errors.items():
                        for error in errors:
                            messages.error(request, f'{field}: {error}')
            except Exception as e:
                messages.error(request, f'An error occurred while sending the email: {str(e)}')
    else:
        form = PasswordResetForm()
    return render(request, 'auth/password_reset.html')



@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your password has been changed successfully.')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'auth/dashboard.html')


@login_required
def profile_view(request):
    return render(request, 'auth/profile.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')
