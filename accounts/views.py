from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email, password=password)
            request.session["user_id"] = user.id
            return redirect('dashboard')
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return render(request, 'login.html', {'email': '', 'password': ''})

    return render(request, 'login.html', {'email': '', 'password': ''})


def dashboard(request):
    if "user_id" not in request.session:
        return redirect("login")
    user = User.objects.get(id=request.session["user_id"])
    return render(request, "dashboard.html", {"user": user})
