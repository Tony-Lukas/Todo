from django.shortcuts import render,redirect
from django.contrib import messages

from .models import TodoItems
from .forms import DetailForm

# Create your views here.
def main(request):
    if request.method == 'POST':
        task = request.POST['task']
        new_task = TodoItems(task=task)
        new_task.save()
        messages.success(request,'New Task added')
        return redirect('main')

    
    items = TodoItems.objects.order_by()
    todo_items = [i for i in items if not i.complete]
    done_items = [i for i in items if i.complete]
    content = {
        'todo_items':todo_items,
        'done_items':done_items,
    }
    return render(request, 'main.html',content)

def add_detail(request,pk):
    current_task = TodoItems.objects.get(id=pk)
    form = DetailForm(request.POST or None,instance=current_task)
    if request.method == 'POST':
        if form.is_valid():
            add_task = form.save()
            messages.success(request,'Done')
            return redirect('main')
    return render(request,'add_detail.html',{'form':form})

def done_task(request,pk):
    task = TodoItems.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect('main')

def delete_task(request,pk):
    task = TodoItems.objects.get(id=pk)
    task.delete()
    messages.success(request,"Sucessfully Deleted!!")
    return redirect('main')
