# 在 views.py 文件中
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MyModel
from .forms import MyModelForm


def upload_file(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # 跳转到成功页面
    else:
        form = MyModelForm()
    return render(request, 'upload.html', {'form': form})


def my_view(request):
    obj = MyModel.objects.get(pk=1)  # 获取数据库中的对象
    return render(request, 'template.html', {'object': obj})


def start(request):
    return render(request, 'welcome.html')


def home_page(request):
    context_dict = {'bold_message': "Crunchy, creamy, cookie, candy, cupcake!"}

    # obj = MyModel.objects.first()
    return render(request, 'homepage.html', {'object': context_dict})


def about(request):
    # 可以在这里编写关于 about 页面的逻辑
    context = {
        'title': 'About Us',
        'content': 'This is the about page content...',
        # 添加其他需要在模板中渲染的数据...
    }
    return render(request, 'about.html', context)
