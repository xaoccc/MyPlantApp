from django.urls import path, include
from MyPlantApp.plant import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
]