from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from MyPlantApp.profiles.models import Profile
from MyPlantApp.plant.models import Plant

class GetProfileMixin:
    def get_object(self, queryset=None):
        return Profile.objects.first()

class PlantDeleteView(DeleteView):
    model = Plant

    def delete(self, request, *args, **kwargs):
        Plant.objects.all().delete()
        return super().delete(request, *args, **kwargs)


class ProfileCreateView(CreateView):
    template_name = 'create-profile.html'
    model = Profile
    fields = ['username', 'first_name', 'last_name']
    def get_success_url(self):
        return reverse('plant-catalogue')


class ProfileDetailView(GetProfileMixin, DetailView):
    model = Profile
    template_name = 'profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plants'] = Plant.objects.all()
        context['plants_count'] = ""
        for star in Plant.objects.all():
            context['plants_count'] += "1"
            if len(context['plants_count']) > 2:
                break

        return context


class ProfileEditView(GetProfileMixin, UpdateView):
    model = Profile
    fields = "__all__"
    template_name = 'edit-profile.html'
    success_url = reverse_lazy("profile-details")


class ProfileDeleteView(GetProfileMixin, DeleteView):
    model = Profile
    template_name = 'delete-profile.html'
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        Plant.objects.all().delete()
        return super().form_valid(form)







