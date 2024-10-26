from django import forms
from .models import TodoItem,TodoGroup
from datetime import datetime, timezone

class GroupForm(forms.ModelForm):
    name = forms.CharField(label="",
                           widget=(forms.widgets.TextInput(attrs={
                               'placeholder':'What Your new projects',
                               'class':'form-control',
                           })))
    class Meta:
        model = TodoGroup
        fields = '__all__'

class DetailForm(forms.ModelForm):
    #cleaned_data = datetime.now(timezone.utc)
    group = forms.ModelChoiceField(TodoGroup.objects.all(),
                                   label='',required=True,
                                    widget=(forms.widgets.Select(attrs={
                                        'class':'form-control',
                                    })))
    task = forms.CharField(label='',required=True, 
                           widget=(forms.widgets.TextInput(attrs={
                               'placeholder':'What is Next?',
                               'class':'form-control',
                           })))
    details = forms.CharField(label='',required=False, 
                           widget=(forms.widgets.TextInput(attrs={
                               'placeholder':'Please Tell me detail?',
                               'class':'form-control',
                               'rows':'5',
                           })))
    complete = forms.BooleanField(label='',
                                widget=(forms.widgets.CheckboxInput()),
                                required=False)
    
    class Meta:
        model = TodoItem
        #fields = ('task','details','states')
        fields = '__all__'