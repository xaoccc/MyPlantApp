from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
# from MyPlantApp.profiles.models import Profile


class ProfileCreateView(TemplateView):
    template_name = 'create-profile.html'

