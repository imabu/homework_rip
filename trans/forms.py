from django import forms
from .models import TransactsModel
from django.contrib.auth.models import User


class TransactsForm(forms.ModelForm):
    class Meta:
        model = TransactsModel
        fields = ('type', 'summ', 'comment', 'pic', 'tags')


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=5, error_messages={'required': 'Введите логин'})
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=30, error_messages={'required': 'Введите email',
                                                            'invalid': 'Введите корректный email'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            return username
        raise forms.ValidationError('Такой логин уже существует')

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(self.cleaned_data.get('username'), self.cleaned_data.get('email'),
                                        self.cleaned_data.get('password1'))
        user.save()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, error_messages={'required': 'Введите логин'})
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password',)


