from django import forms
from .models import online_zapis

class online_zapis_form(forms.ModelForm):
    class Meta:
        model=online_zapis
        fields=['name','place','phone_number','date','time','main_text']



        
