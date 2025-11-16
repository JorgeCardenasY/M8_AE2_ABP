from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            print(form.cleaned_data)
            return redirect('index')  # Redirect to a 'thank you' page or home
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def analytics(request):
    return render(request, 'analytics.html')