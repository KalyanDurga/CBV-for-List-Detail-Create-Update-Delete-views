from django.shortcuts import render

# Create your views here.
from app.models import *
from django.urls import reverse_lazy

from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView

class home(TemplateView):
    template_name='app/home.html'

class list_school(ListView):
    model=School
    context_object_name='schools'

class schooldetail(DetailView):
    model=School
    context_object_name='scl'

class schoolcreate(CreateView):
    model=School
    fields='__all__'


class schoolupdate(UpdateView):
    model=School
    fields='__all__'

class schooldelete(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('list_school')
