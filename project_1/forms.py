from django import forms
from .models import MyModel


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', min_length=4, max_length=64, error_messages={
                                   'min_length': "密码长度不能小于4个字符",
                                   'max_length': "密码长度不能大于64个字符"})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['my_file', 'my_image', 'my_url', 'my_field', 'my_integer', 'my_date']  # 指定表单包含的字段，这里只包含 my_image 字段


# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']