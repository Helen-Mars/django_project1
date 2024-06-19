# 在 views.py 文件中
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MyModel, CustomUser
from .forms import MyModelForm, UserRegistrationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def success_page(request):
    return render(request, 'success_page.html')


class RegisterUser(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')  # 注册成功后重定向到登录页面


def upload_file(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # 跳转到成功页面
    else:
        form = MyModelForm()
    return render(request, 'upload.html', {'form': form})


def start(request):
    return render(request, 'welcome.html')


def home_page(request):
    text = "hello Django"

    # obj = MyModel.objects.first()
    return render(request, 'homepage.html', {'text': text})


def about(request):
    # 可以在这里编写关于 about 页面的逻辑
    context = {
        'title': 'About Us',
        'content': 'This is the about page content...',
        # 添加其他需要在模板中渲染的数据...
    }
    return render(request, 'about.html', context)
