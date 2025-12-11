from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email',"")
        password = request.POST.get('password',"")
        try:
            user = User.objects.get(email = email,password = password)
            request.session["user_id"] = user.id
            return redirect('dashboard')
        except User.DoesNotExist:
            messages.error(request,"invalid or credits")
            return (request,'login')
    
            
    return render(request,'login.html')



def dashboard(request):
    return render(request,'dashboard.html')