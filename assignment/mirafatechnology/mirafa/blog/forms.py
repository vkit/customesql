from django import forms
from django.contrib.auth import authenticate


class AuthForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=100)
    pasword = forms.CharField(label='password', max_length=50)

# class AuthForm(forms.Form):
#     user_name = forms.CharField(label='Your name', max_length=100)
#     pasword = forms.CharField(widget=forms.PasswordInput)

#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data('username')
#         password = self.cleaned_data('password')
#         user = authenticate(username=username, password=password)

#         if not user:
#             raise forms.ValidationError("This user does not exist")
#         if not user.check_password(password):
#             raise forms.ValidationError("password deos not exists")
#         return super(AuthForm, self).clean(*args, **kwargs)