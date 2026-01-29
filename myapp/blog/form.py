from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label='Your Name',
        required=True,
        error_messages={'required': 'Please enter your name'}
    )
    email = forms.EmailField(
        label='Your Email',
        required=True,
        error_messages={
            'required': 'Please enter your email address',
            'invalid': 'Please enter a valid email address'
        }
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Your Message',
        required=True,
        error_messages={'required': 'Please enter your message'}
    )