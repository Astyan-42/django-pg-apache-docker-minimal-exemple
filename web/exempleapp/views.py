from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from exempleapp.models import ExempleDB
from django.urls import reverse_lazy


# Create your views here.
class ExempleListView(ListView):
    context_object_name = 'exemple_list'
    template_name = 'exempleapp/showexemple.html'
    model = ExempleDB


class ExempleCreateView(CreateView):
    model = ExempleDB
    template_name = 'exempleapp/addexemple.html'
    fields = ['name']
    success_url = reverse_lazy('index')
