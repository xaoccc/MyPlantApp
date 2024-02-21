from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, UpdateView, ListView
from MyPlantApp.profiles.models import Profile
from MyPlantApp.plant.forms import DeletePlantForm
from MyPlantApp.plant.models import Plant
class GetProfileMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context

class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
        return form


# Create your views here.
class HomePageView(GetProfileMixin, TemplateView):
    template_name = 'home-page.html'


class CreatePlantView(GetProfileMixin, CreateView):
    template_name = 'create-plant.html'
    model = Plant
    fields = "__all__"

    def get_success_url(self):
        return reverse('plant-catalogue')

class CataloguePlantView(GetProfileMixin, ListView):
    template_name = 'catalogue.html'
    model = Plant
    context_object_name = 'plants'


class DetailsPlantView(GetProfileMixin, DetailView):
    template_name = 'plant-details.html'
    model = Plant


class EditPlantView(GetProfileMixin, UpdateView):
    template_name = 'edit-plant.html'
    model = Plant
    fields = "__all__"

    def get_success_url(self):
        return reverse('plant-catalogue')



class DeletePlantView(GetProfileMixin, ReadOnlyMixin, DeleteView):
    template_name = 'delete-plant.html'
    model = Plant
    form_class = DeletePlantForm

    def get_success_url(self):
        return reverse('plant-catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
