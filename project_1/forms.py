from django import forms
from .models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['my_file', 'my_image', 'my_url', 'my_field', 'my_integer', 'my_date']  # 指定表单包含的字段，这里只包含 my_image 字段
