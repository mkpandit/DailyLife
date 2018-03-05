from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddTodo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import to_do_list
from django.utils import timezone

#view method to serve the home page.
def index(request):
    #this option gets all the items
    to_do_list_sorted = to_do_list.objects.order_by('to_do_time')

    #this option gets items which has a valid date - currently disabled. if enabled the previous line should be disabled
    #to_do_list_sorted = to_do_list.objects.filter(to_do_time__gte=timezone.now())

    #generate the paginator
    paginator = Paginator(to_do_list_sorted, 9)
    page = request.GET.get('page', 1)

    try:
        to_do_list_paged = paginator.page(page)
    except PageNotAnInteger:
        to_do_list_paged = paginator.page(1)
    except EmptyPage:
        to_do_list_paged = paginator.page(paginator.num_pages)

    return render(request, 'todolist/index.html', {'to_do_list_paged': to_do_list_paged})

#view method to serev the search function
def search(request):
    term = request.GET.get('term')
    if term:
        message = 'You searched for: %r' % request.GET['term']
    else:
        message = 'You submitted an empty form'

    #filter the items based on the keyword provided, currentl it checks only the title of the to_do_list
    to_do_list_filtered = to_do_list.objects.filter(to_do_title__contains=term)#.filter(description__contains=term)

    #generate the paginator
    paginator = Paginator(to_do_list_filtered, 10)
    page = request.GET.get('page', 1)

    try:
        to_do_list_paged = paginator.page(page)
    except PageNotAnInteger:
        to_do_list_paged = paginator.page(1)
    except EmptyPage:
        to_do_list_paged = paginator.page(paginator.num_pages)

    return render(request, 'todolist/search.html', {'message': message, 'term': term, 'to_do_list_paged': to_do_list_paged})

#view method to serve the to-do item detailed page
def to_do_detail(request, pk):
    to_do_details = get_object_or_404(to_do_list, pk=pk)
    return render(request, 'todolist/details.html', {'to_do_details': to_do_details})

#view method to delete an item
def to_do_delete(request, pk):
    to_do_delete = to_do_list.objects.get(id=pk)
    if to_do_delete.delete():
        return redirect('home')

#view method (modelForm) to add a new item
def add_todo(request):
    if request.method == 'POST':
        form = AddTodo(request.POST, request.FILES)
        if form.is_valid():
            client=form.save(commit=False)
            client.to_do_time = form.cleaned_data['to_do_time']
            client.to_do_title = form.cleaned_data['to_do_title']
            client.description = form.cleaned_data['description']
            client.save()
            return redirect('home')
    else:
        form = AddTodo()
    return render(request, 'todolist/add_todo.html', {'form' : form})

#view methos to edit an item
def edit_todo(request, pk):
    to_do = get_object_or_404(to_do_list, pk=pk)
    form = AddTodo(request.POST or None, instance=to_do)
    if request.method == 'POST':
        if form.is_valid():
            #client = form.save(commit=False)
            #client.to_do_time = form.cleaned_data['to_do_time']
            #client.to_do_title = form.cleaned_data['to_do_title']
            #client.description = form.cleaned_data['description']
            #client.save()
            form.save()
            return redirect('todo_details', pk=to_do.pk)
    else:
        form = AddTodo(instance=to_do)
    return render(request, 'todolist/edit_todo.html', {'form': form})