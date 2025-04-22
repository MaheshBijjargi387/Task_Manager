from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from .forms import*

def create_task(request):
    form=TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_task') 
   
    return render(request, 'create_task.html', {'form': form})
        
def view_task(request):
    task=Task.objects.all()
    return render(request,'task_list.html',{'tasks':task})



def delete_task(request, id):
    task = get_object_or_404(Task, id=id)  
    task.delete()
    return redirect('view_task')  



def update_task(request, id):
    task = get_object_or_404(Task, id=id) 
    form = TaskForm(instance=task) 
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  
        if form.is_valid():
            form.save()  
            return redirect('view_task')  
        
    return render(request, 'update_task.html', {'form': form, 'task': task})
