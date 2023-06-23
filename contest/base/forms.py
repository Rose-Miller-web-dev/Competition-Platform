from django.forms import ModelForm
from .models import Competition, CustomUser

class UpdateCompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = ['topic', 'title', 'description', 'price']

class CreateCompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'
        exclude = ['host', 'competitors']
