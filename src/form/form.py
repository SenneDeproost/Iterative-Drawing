from django import forms


# Registration form for new users
class RegistrationForm(forms.Form):

    first_name = forms.CharField(label='Enter your first name', max_length=100)
    last_name = forms.CharField(label='Enter your last name', max_length=100)
    age = forms.IntegerField(label='Enter your age', min_value=0, max_value=150)
    email = forms.EmailField(label='Enter your email', max_length=100)
