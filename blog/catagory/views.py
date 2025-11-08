from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Catagory
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from .form import cata_form

class catagory_list(ListView):
    model = Catagory
    template_name = 'catagory.html'
    context_object_name = 'topic'


class createview(CreateView):
    model = Catagory
    template_name = 'cata_create.html'
    # fields = ['name','parent']
    success_url = reverse_lazy('all_Post')
    form_class = cata_form


class updateView(UpdateView):
    model = Catagory
    template_name = "cata_update.html"
    # fields = ['name','parent']
    success_url = reverse_lazy('all_Post')
    form_class = cata_form

class deleteView(DeleteView):
    model = Catagory
    template_name = "cata_delete.html"
    success_url = reverse_lazy('all_Post')

def cata_post(request,id):
    pass



