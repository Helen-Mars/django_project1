# 在 views.py 文件中
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MyModel, CustomUser
from .forms import MyModelForm, UserRegistrationForm, LoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))

    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # 增加访问次数后更新“last_visit”cookie
        request.session['last_visit'] = str(datetime.now())
    else:
        # 设定“last_visit”
        request.session['last_visit'] = last_visit_cookie
        # 更
    request.session['visits'] = visits


def logout_view(request):
    logout(request)
    # 可选：执行额外的清理操作
    # 记录日志、发送邮件等

    # 重定向到登录页面或其它页面
    return redirect('home')  # 假设 'login' 是你的登录页面的 URL 名称


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username'].strip()
            password = request.POST['password'].strip()
            # 打印出来检查值
            print(f"Username: {username}, Password: {password}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # 登录成功后的跳转逻辑，例如重定向到首页
                messages.success(request, '登录成功！')
                return redirect('home')
            else:
                # 登录失败处理
                print("Authentication failed: user is None")

                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
        else:
            print("Form is invalid:", form.errors)
    else:
        form = LoginForm()
    # 渲染登录页面
    return render(request, 'login.html', {'form': form})


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

    visitor_cookie_handler(request)

    text = "hello Django"
    # obj = MyModel.objects.first()
    return render(request, 'homepage.html', {'text': text, 'visits': request.session['visits']})


@login_required
def about(request):
    # 可以在这里编写关于 about 页面的逻辑
    # request.session.set_test_cookie()
    # if request.session.test_cookie_worked():
    #     print("TEST COOKIE WORKED!")
    #     request.session.delete_test_cookie()

    context = {
        'title': 'About Us',
        'content': 'This is the about page content...',
        # 添加其他需要在模板中渲染的数据...
    }
    return render(request, 'about.html', context)
