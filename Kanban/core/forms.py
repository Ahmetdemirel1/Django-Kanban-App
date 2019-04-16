from django import forms
from core.models import *



class KanbanCardForm(forms.ModelForm):
    title = forms.CharField(max_length=35, widget=forms.TextInput(attrs={'placeholder': 'Başlık'}), required=False)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama'}))
    status = forms.ChoiceField(widget=forms.Select(), choices=status, required=False)

    class Meta:
        model = KanbanModel
        fields = ('title', 'description', 'status')