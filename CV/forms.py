from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Tu nombre"}),
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"placeholder": "tu@email.com"}),
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={"placeholder": "Escribe tu mensaje aquí..."}),
    )
