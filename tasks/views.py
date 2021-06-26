from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView,UpdateView
from django.views.decorators.csrf import csrf_exempt
from .models import Tasks
from tasks.forms import createTask

#base.html podemos agrupar codigo que se repite en las distintas views, como el navbar

def home(request):
    #return with render is still returning an HttpResponse 
    
    context = {
        'styleFolder' : 'css/index.css'
    }
    return render(request,'tasks/index.html',context)

@login_required
def tareas(request):
    if request.method == 'POST':
        newTask_form = createTask(request.POST)
        if newTask_form.is_valid():
            newTask = newTask_form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            newTask_form = createTask()
            return redirect('tasks-tareas')

    else:
        newTask_form = createTask()
    context = {
        'styleFolder' : 'css/tasks.css',
        'tasks' : Tasks.objects.filter(user=request.user.id),
        'newTask_form': newTask_form
        }
    return render(request,'tasks/tasks.html',context)


@csrf_exempt
@login_required
def start_task(request,pk):
    if request.method == 'POST':
        tarea = Tasks.objects.filter(id=pk)
        if request.user == tarea[0].user:
            tarea.update(state='EP')
            data = {
                'title' : tarea[0].title,
                'subtitle' : tarea[0].subtitle,
                'limit_date' : tarea[0].limit_date,
                'description' : tarea[0].description,
                'id' : tarea[0].id
            }
            return JsonResponse(data)


@csrf_exempt
@login_required
def end_task(request,pk):
    if request.method == 'POST':
        tarea = Tasks.objects.filter(id=pk)
        if request.user == tarea[0].user:
            tarea.update(state='FN')
            data = {
                'title' : tarea[0].title,
                'subtitle' : tarea[0].subtitle,
                'limit_date' : tarea[0].limit_date,
                'description' : tarea[0].description,
                'id' : tarea[0].id
            }
            return JsonResponse(data)

class updateTaskView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tasks
    fields = ['title', 'subtitle', 'limit_date', 'description', 'state']
    template_name = 'tasks/updateTasks.html'
    success_url = '/tasks/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        else:
            return False

class deleteTaskView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/deleteTask.html'
    success_url = '/tasks/'
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        else:
            return False