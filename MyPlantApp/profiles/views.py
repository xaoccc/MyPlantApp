from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from MyPlantApp.profiles.models import Profile


class ProfileCreateView(CreateView):
    template_name = 'create-profile.html'
    model = Profile
    fields = ['username', 'first_name', 'last_name']
    def get_success_url(self):
        return reverse('plant-catalogue')

