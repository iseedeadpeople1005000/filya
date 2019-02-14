from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import get_user_model
User = get_user_model()
from . import form

def out(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пожалуйста, введите правильные имя пользователя и пароль.'
            return render(request, 'log.html', args)
    else:
        return render(request, 'log.html', args)

def sign(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        try:
            user = User.objects.create_user(username=request.POST.get('username', ""),
                                            email=request.POST.get('email',""),
                                            password=request.POST.get('password',""))
        except:
            user = None

        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            args["sign_error"] = "Пользователь уже существует"
            return render(request, "sign.html", args)
    else:
        return render(request, 'sign.html', args)


def hello(request):
    return HttpResponse("<h1>hello</h1>")
