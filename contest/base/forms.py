from django.forms import ModelForm
from .models import Competition

class CompetitionForm(ModelForm):
    class Meta:
        model = Competition
        fields = ['topic', 'title', 'description']
