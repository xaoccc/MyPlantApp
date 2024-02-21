from django.urls import path, include
from MyPlantApp.profiles import views

urlpatterns = [
    path('create', views.ProfileCreateView.as_view(), name='profile-create'),
]