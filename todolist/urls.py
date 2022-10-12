from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_todo, name='show_create_todo'),
    path('delete/<int:pk>', delete, name='delete'),
    path('change/<int:pk>', change, name='change'),
    path('json/', show_json, name='show_json'),
    path('add/', add_ajax, name='add_ajax'),
]