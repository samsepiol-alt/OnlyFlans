from django import forms
from web.models import ContactForm



class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name','customer_email','message']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@ejemplo.cl'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mensaje'}),
        }
        error_messages = {
            'customer_name': {
                'required': 'El nombre es obligatorio.',
                'max_length': 'El nombre no puede tener más de 64 caracteres.'
            },
            'customer_email': {
                'required': 'El correo electrónico es obligatorio.',
                'invalid': 'Introduce una dirección de correo válida.'
            },
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message or message.strip() == "":
            raise forms.ValidationError("El mensaje no puede estar vacío.")
        return message



class ContactFormForm(forms.Form):
    customer_name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        error_messages={
            'required': 'El nombre es obligatorio.',
            'max_length': 'El nombre no puede tener más de 64 caracteres.'
        }
    )
    
    customer_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@ejemplo.cl'}),
        error_messages={
            'required': 'El correo electrónico es obligatorio.',
            'invalid': 'Introduce una dirección de correo válida.'
        }
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mensaje'}),
        error_messages={
            'required': 'El mensaje no puede estar vacío.'
        }
    )

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message or message.strip() == "":
            raise forms.ValidationError("El mensaje no puede estar vacío.")
        return message
