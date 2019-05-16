from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        '''
        help_texts = {'username': None, 'email': None, 'password1': None, 'password2': None}
        for some reason changing help_text does not work, so I did that 
        with overiding __init__ method (shown above)
        '''
