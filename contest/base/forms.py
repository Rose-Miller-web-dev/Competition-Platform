from django.forms import ModelForm
from .models import Competition

class UpdateCompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = ['topic', 'title', 'description']

class CreateCompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
