from django.shortcuts import render, redirect
from .models import Item
from .forms import Itemform


# Create your views here.
def get_todolist(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_items(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todolist')
    form = Itemform()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
