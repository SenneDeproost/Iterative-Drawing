from django import forms


# Registration form for new users
class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Age', min_value=0, max_value=150)
    email = forms.EmailField(label='E-mail', max_length=100)
