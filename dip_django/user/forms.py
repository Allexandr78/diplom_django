''' Форма профиля '''
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    """ Форма профиля """
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        """ Описание модели и полей для формы """
        model = Profile
        fields = ["image", "first_name", "last_name", "email"]
