from django.shortcuts import render,redirect
from application.models import enquiry_table, ServiceBooking
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
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
def success(request):
    return render(request, 'success.html')
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
            return render(request, 'success.html')
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
    return render(request, 'custom_dashboard.html')

from django.shortcuts import render, redirect
from .forms import ServiceBookingForm

def book_service(request):
    if request.method == "POST":
        form = ServiceBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect after booking
    else:
        form = ServiceBookingForm()
    return render(request, 'service_booking.html', {'form': form})

#admin fetch 

@staff_member_required
def admin_dashboard(request):
    #--Enquiry--

    enquiry_search = request.GET.get("enquiry_search", "")
    enquiry_date = request.GET.get("enquiry_date","")

    enquiries = enquiry_table.objects.all().order_by("-created_at")
    if enquiry_search:
        enquiries = enquiries.filter(
            Q(name_icontains=enquiry_search) |
            Q(email_icontains=enquiry_search) |
            Q(phone_icontains=enquiry_search) |
            Q(messages_icontains=enquiry_search)
        )

    if enquiry_date:
        enquiries = enquiries.filter(created_at_date=enquiry_date)

# --- Bookings ---
    booking_search = request.GET.get("booking_search", "")
    booking_date = request.GET.get("booking_date", "")
    service_type = request.GET.get("service_type", "")

    bookings = ServiceBooking.objects.all().order_by("-created_at")
    if booking_search:
        bookings = bookings.filter(
            Q(name__icontains=booking_search) |
            Q(email__icontains=booking_search) |
            Q(phone__icontains=booking_search) |
            Q(message__icontains=booking_search)
        )
    if booking_date:
        bookings = bookings.filter(appointment_date=booking_date)
    if service_type:
        bookings = bookings.filter(service_type=service_type)

    return render(request, "custom_dashboard.html", {
        "enquiries": enquiries,
        "bookings": bookings,
    })
