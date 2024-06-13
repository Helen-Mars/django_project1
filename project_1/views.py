# 在 views.py 文件中
from django.http import HttpResponse
from django.shortcuts import render

def start(request):

    return HttpResponse("Please enter!")

def home_page(request):
    context_dict = {'bold_message': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'homepage.html', context=context_dict)


def about(request):
    # 可以在这里编写关于 about 页面的逻辑
    context = {
        'title': 'About Us',
        'content': 'This is the about page content...',
        # 添加其他需要在模板中渲染的数据...
    }
    return render(request, 'about.html', context)