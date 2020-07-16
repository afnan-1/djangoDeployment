from django import forms
from protwo.models import User
class NewUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name']
        
