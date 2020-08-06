from django.forms import ModelForm
from .models import Bb


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'rubric', 'char1', 'items1', 'char2', 'items2', 'char3', 'items3', 'char4', 'items4')
