from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import CharField

class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length = 500, help_text = 'Something that describes you in brief?')
    cc_handle = forms.CharField(max_length = 40)
    cf_handle = forms.CharField(max_length=40)
    sp_handle = forms.CharField(max_length=40)
    ac_handle = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ('username', 'bio', 'cc_handle', 'cf_handle', 'sp_handle', 'ac_handle', 'password1', 'password2',)