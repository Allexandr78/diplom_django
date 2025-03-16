''' Форма профиля '''
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    ''' Форма профиля '''
    class Meta:
        ''' Мета класс '''
        model = Profile
        fields = ['image']
