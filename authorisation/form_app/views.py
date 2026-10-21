from django.shortcuts import redirect, render

from .form import ContactForm
from .models import Contact


def index(request):
    return render(request, 'form_app/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()

            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )



            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'form_app/contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')

def contact_list_view(request):
    contacts = Contact.objects.all()
    return render(request, 'form_app/contact_list.html', {'contacts': contacts})
