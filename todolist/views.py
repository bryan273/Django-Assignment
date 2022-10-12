import datetime
from django.shortcuts import render, redirect
from todolist.models import TodoListEntry
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login/')
def show_todolist(request):
    data_todo = TodoListEntry.objects.filter(user=request.user)

    context = {
    'list_todo': data_todo,
    'nama': 'Bryan Tjandra',
    'username' :  request.user.username,
    }
    return render(request, "todolist.html",context=context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def show_create_todo(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('deskripsi')
        is_finished = False
        todo = TodoListEntry.objects.create(title=title, 
                                            description=description,
                                            date=datetime.date.today(), 
                                            user=request.user,
                                            is_finished=is_finished)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response

    return render(request, "create.html")

# butuh diubah
@csrf_exempt  
def delete(request, pk):
    TodoListEntry.objects.filter(id=pk).delete()
    return redirect('todolist:show_todolist')

def change(request, pk):
    data = TodoListEntry.objects.get(id=pk)
    data.is_finished = not(data.is_finished)
    data.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    user = TodoListEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', user), content_type='application/json')

@login_required(login_url='/todolist/login/')
def add_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('nama')
        description = request.POST.get('desc')
        is_finished = False
        todo = TodoListEntry.objects.create(title=title, 
                                            description=description,
                                            date=datetime.date.today(), 
                                            user=request.user,
                                            is_finished=is_finished)
        todo.save()
        
        result = {
            'fields':{
                'title':todo.title,
                'description':todo.description,
                'is_finished':todo.is_finished,
                'date':todo.date,
            },
            'pk':todo.pk
        }
        return JsonResponse(result,status=200)