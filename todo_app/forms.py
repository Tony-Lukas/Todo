from django import forms
from .models import TodoItems
from datetime import datetime, timezone

class DetailForm(forms.ModelForm):
    cleaned_data = datetime.now(timezone.utc)
    task = forms.CharField(label='',required=True, 
                           widget=(forms.widgets.TextInput(attrs={
                               'placeholder':'What is Next?',
                               'class':'form-control',
                           })))
    details = forms.CharField(label='',required=False, 
                           widget=(forms.widgets.Textarea(attrs={
                               'placeholder':'Please Tell me detail?',
                               'class':'form-control',
                               'rows':'5',
                           })))
    complete = forms.BooleanField()#label='',
                                #widget=(forms.widgets.CheckboxInput()),
                                #required=False)
    
    class Meta:
        model = TodoItems
        #fields = ('task','details','states')
        fields = '__all__'