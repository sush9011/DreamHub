from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration
# Create your views here.
#index page and form
def index(request):
    return render(request,'index.html')
#about page 
def about(request):
    return render(request, 'about.html')

#contact page and form
def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Log and ensure data is coming through
        print(f"Received data: Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")

        # Validate fields are not empty
        if not all([name, email, phone, message]):
            messages.error(request, "All fields are required.")
            return render(request, 'contact.html')

        # Save to the Registration model (ensure no exceptions)
        try:
            registration = Registration.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )
            messages.success(request, "Your details have been submitted successfully.")
            return redirect('contact')
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return render(request, 'contact.html')

    return render(request, 'contact.html')  # Show the form if GET request