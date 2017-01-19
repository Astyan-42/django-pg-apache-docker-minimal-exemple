from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView

# Create your views here.
class UserListView(ListView):
    context_object_name = 'user_list'
    template_name = 'showusers/showusers.html'
    model = get_user_model()
