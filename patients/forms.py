from django import forms
from records.models import FileNumber

class FileNumberForm(forms.ModelForm):
    class Meta:
        model = FileNumber
        fields = '__all__'