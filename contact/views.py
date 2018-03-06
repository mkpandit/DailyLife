from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import AddContact

# Create your views here.

def index(request):
    contact = Contact.objects.order_by('first_name')
    return render(request, 'contact/index.html', {'contact':contact})

def contactDetail(request, pk):
    contact_details = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/details.html', {'contact_details': contact_details})

def addContact(request):
    if request.method == 'POST':
        form = AddContact(request.POST, request.FILES)
        if form.is_valid():
            entry=form.save(commit=False)
            entry.first_name = form.cleaned_data['first_name']
            entry.last_name = form.cleaned_data['last_name']
            entry.phone_number = form.cleaned_data['phone_number']
            entry.email_address = form.cleaned_data['email_address']
            entry.postal_address = form.cleaned_data['postal_address']
            entry.country = form.cleaned_data['country']
            entry.save()
            return redirect('contact_home')
    else:
        form = AddContact
    return render(request, 'contact/add.html', {'form' : form})

#view methos to edit an item
def editContact(request, pk):
    con = get_object_or_404(Contact, pk=pk)
    form = AddContact(request.POST or None, request.FILES, instance=con)
    if request.method == 'POST':
        if form.is_valid():
            #client = form.save(commit=False)
            #client.to_do_time = form.cleaned_data['to_do_time']
            #client.to_do_title = form.cleaned_data['to_do_title']
            #client.description = form.cleaned_data['description']
            #client.save()
            form.save()
            return redirect('contact_details', pk=con.pk)
    else:
        form = AddContact(instance=con)
    return render(request, 'contact/edit.html', {'form': form})