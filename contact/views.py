from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import AddContact

# Create your views here.

def index(request):
    contact = Contact.objects.order_by('first_name')
    return render(request, 'contact/index.html', {'contact':contact})

def addContact(request):
    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            entry=form.save(commit=False)
            entry.first_name = form.cleaned_data['first_name']
            entry.last_name = form.cleaned_data['last_name']
            entry.phone_number = form.cleaned_data['phone_number']
            entry.email_address = form.cleaned_data['email_address']
            entry.postal_address = form.cleaned_data['postal_address']
            entry.country = form.cleaned_data['country']
            entry.save()
            return redirect('home')
    else:
        form = AddContact
    return render(request, 'contact/add.html', {'form' : form})