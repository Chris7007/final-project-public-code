from django.forms import ModelForm, Textarea
from .models import *


class ReportForm(ModelForm):
    class Meta:
        model = Reports
        fields = {'report'}
        widgets = {
            'report': Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5})
            }
