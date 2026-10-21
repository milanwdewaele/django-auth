from django.shortcuts import redirect, render

from .form import ContactForm
from .models import Contact

from django.contrib.auth import logout

from .decorators import group_required


@group_required("defaultUsers", "superUsers")
def index(request):
    is_super_user = request.user.groups.filter(name="superUsers").exists()
    return render(
        request,
        "form_app/index.html",
        {"is_super_user": is_super_user},
    )


@group_required("defaultUsers", "superUsers")
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()

            Contact.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
            )

            return redirect("success")
    else:
        form = ContactForm()

    return render(request, "form_app/contact.html", {"form": form})


@group_required("defaultUsers", "superUsers")
def contact_success_view(request):
    return render(request, "form_app/contact_success.html")


@group_required("superUsers")
def contact_list_view(request):
    contacts = Contact.objects.all()
    return render(
        request,
        "form_app/contact_list.html",
        {"contacts": contacts},
    )


def logout_view(request):
    logout(request)
    return redirect("login")