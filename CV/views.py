from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f'Nuevo mensaje de contacto de {name}'
            email_message = f'Nombre: {name}\n' \
                            f'Email: {email}\n\n' \
                            f'Mensaje:\n{message}'
            
            from_email = 'noreply@portafolio.com'
            recipient_list = ['jorge.cardenas.y@gmail.com']

            send_mail(subject, email_message, from_email, recipient_list)

            return redirect('confirmation') # Redirect to confirmation page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def analytics(request):
    return render(request, 'analytics.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def proyectos(request):
    return render(request, 'proyectos.html')