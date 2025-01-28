from django.shortcuts import render,redirect
from application.models import enquiry_table
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.
#index page and form
def index(request):
    return render(request,'index.html')
#about page 
def about(request):
    return render(request, 'about.html')
#services
def ceramic(request):
    return render(request,'ceramic.html')
def ppf(request):
    return render(request,'ppf.html')
def wrap(request):
    return render(request,'wrap.html')
def detailing(request):
    return render(request,'detailing.html')
def denting(request):
    return render(request,'denting.html')
def insurance(request):
    return render(request,'insurance.html')
def other(request):
    return render(request,'other.html')
#maste page
@login_required
def master_page(request):
    return render(request, 'master_page.html')



#contact page and form
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        enquiry = enquiry_table(name = name, email = email, phone = phone, message = message)
        try:
            enquiry.save()
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
        
    return render(request, 'contact.html')

#login code made by sushant
@csrf_exempt
def admin_login(request):  # Avoid naming conflicts
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                auth_login(request, user)  # Properly using Django's login function
                return redirect('master_page')
            else:
                messages.error(request, 'Invalid username or password.')
                
    return render(request, 'login.html')

def logout_user(request):
    auth_logout(request)
    return redirect('login')

def admin_page(request):
    from django.http import HttpResponseForbidden
    if not request.user.is_staff:
        return HttpResponseForbidden('You are not authorized to view this page.')
    return render(request, '/admin/')

