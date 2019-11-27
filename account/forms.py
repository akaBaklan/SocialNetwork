from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    re_entered_password = forms.CharField(label='Password',
                                        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_re_entered_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_entered_password']:
            raise forms.ValidationError("Passwords does't match")
        return cd['password']
