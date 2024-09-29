from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Personnel
from django.shortcuts import render

# Fetch
class PersonnelListView(ListView):
    model = Personnel
    template_name = 'personnel_list.html'
    context_object_name = 'personnels'
    

# Fetch by id
class PersonnelDetailView(DetailView):
    model = Personnel
    template_name = 'personnel_detail.html'
    context_object_name = 'personnel'

# Create
class PersonnelCreateView(CreateView):
    model = Personnel
    template_name = 'personnel_form.html'
    fields = ['nom', 'prenom', 'fonction', 'telephone', 'email', 'adresse']
    success_url = reverse_lazy('personnel_list')

# update
class PersonnelUpdateView(UpdateView):
    model = Personnel
    template_name = 'personnel_form.html'
    fields = ['nom', 'prenom', 'fonction', 'telephone', 'email', 'adresse']
    success_url = reverse_lazy('personnel_list')

# Delete
class PersonnelDeleteView(DeleteView):
    model = Personnel
    template_name = 'personnel_delete.html'
    success_url = reverse_lazy('personnel_list')

#home
def home(request):
    return render(request, 'home.html')