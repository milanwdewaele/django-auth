
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

    def send_email(self):
        print(f"Sending email from {self.cleaned_data['name']} <{self.cleaned_data['email']}>: {self.cleaned_data['message']}")