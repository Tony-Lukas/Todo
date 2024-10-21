from django.shortcuts import render,redirect
from django.contrib import messages

from .models import TodoItem,TodoGroup
from .forms import DetailForm,GroupForm

# Create your views here.
def main(request):
    todo_groups = TodoGroup.objects.all()

    form = GroupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,'New Group is added')
        return redirect('main')
    context = {
        'form':form,
        'todo_groups':todo_groups,

    }
    return render(request,'main.html',context)

def item_main(request,group_id):
    group = TodoGroup.objects.get(id=group_id)
    items = group.todoitem_set.all()
    form = DetailForm(request.POST or None)
    context = {
        'items':items,
        'group':group,
        'form':form,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('item_main',group_id=group.id)

    return render(request, 'item_main.html',context)

def add_detail(request,pk):
    current_task = TodoItem.objects.get(id=pk)
    form = DetailForm(request.POST or None,instance=current_task)
    if request.method == 'POST':
        if form.is_valid():
            add_task = form.save()
            messages.success(request,'Done')
            return redirect('item_main',group_id=current_task.group.id)
    return render(request,'add_detail.html',{'form':form})

def done_task(request,pk):
    task = TodoItem.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect('item_main',group_id=task.group.id)

def delete_task(request,pk):
    task = TodoItem.objects.get(id=pk)
    task.delete()
    messages.success(request,f"{task} Deleted!!")
    return redirect('item_main',group_id=task.group.id)

def delete_group(request,group_id):
    group =TodoGroup.objects.get(id=group_id)
    group.delete()
    messages.success(request,f'{group} Deleted')
    return redirect('main')

def update_group(request,group_id):
    group = TodoGroup.objects.get(id=group_id)
    form = GroupForm(request.POST or None,instance=group)
    context = {
        'form':form,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request,'group_update_form.html',context)
