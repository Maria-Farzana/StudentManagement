from django.forms import ModelForm
from .models import *

class FarzanaForm(ModelForm):
    class Meta:
        model=management
        fields='__all__'
