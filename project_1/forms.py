from django import forms
from .models import MyModel, CustomUser
from django.contrib.auth.forms import UserCreationForm


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['my_file', 'my_image', 'my_url', 'my_field', 'my_integer', 'my_date']  # 指定表单包含的字段，这里只包含 my_image 字段


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']