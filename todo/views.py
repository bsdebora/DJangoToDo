from django.shortcuts import render, redirect
from .models import Item


# Create your views here.
def get_todolist(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_items(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todolist')
    return render(request, 'todo/add_item.html')
