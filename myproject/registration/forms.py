from django import forms 

class SignUp(forms.Form):
    first_name = forms.CharField(initial='First Name',)
    last_name = forms.CharField()
    email = forms.EmailField(help_text='Write you email',)
    address = forms.CharField(required=False, )
    technology = forms.CharField(initial='Django', disabled=True, )
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(help_text='renter your password ', widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError("Password is too short!")
        return password