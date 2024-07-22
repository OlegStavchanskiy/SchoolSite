from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import PasswordInput, ModelForm
from django.core.validators import validate_email
from mainpage.models import Article


# форма авторизации
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Пароль')


class PublishNews(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
    title = forms.CharField(required=True, label='Заголовок')
    text = forms.Textarea()
    def clean(self):
        cleaned_data = super(PublishNews, self).clean()
        return cleaned_data