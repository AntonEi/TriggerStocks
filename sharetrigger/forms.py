from django import forms
from .models import sharetrigger

class SharetriggerForm(forms.ModelForm):
    class Meta:
        model = sharetrigger
        fields = ['suggest_stock', 'suggest_date', 'suggest_summary', 
                  'more_info', 'suggest_pr']
