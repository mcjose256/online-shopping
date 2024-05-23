
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:home')  # Redirect to a different page after login
        else:
            # Add a message to inform the user that login failed
            return render(request, 'accounts/login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})