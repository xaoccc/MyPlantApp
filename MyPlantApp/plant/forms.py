from django import forms
from MyPlantApp.plant.models import Plant

class DeletePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"