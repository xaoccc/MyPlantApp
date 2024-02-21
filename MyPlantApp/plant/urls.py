from django.urls import path, include
from MyPlantApp.plant import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('create/', views.CreatePlantView.as_view(), name='plant-create'),
    path('catalogue/', views.CataloguePlantView.as_view(), name='plant-catalogue'),
    path('details/<int:pk>/', views.DetailsPlantView.as_view(), name='plant-details'),
    path('edit/<int:pk>/', views.EditPlantView.as_view(), name='plant-edit'),
    path('delete/<int:pk>/', views.DeletePlantView.as_view(), name='plant-delete'),

]