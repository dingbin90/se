from django.shortcuts import render,redirect,HttpResponseRedirect

# Create your views here.
from ad import models



def index(request):

    pass
    return render(request,'index.html')

d


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = "所有字段都必须填写！"
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name = username)
                print(user.name)
                print('###########3')
                print(user.passwd)
                if user.passwd == password:
                    return redirect('index/')
                else:
                    message = "密码不正确"
            except:
               message = "用户不存在"
        # print(username,password)
        return render(request, 'login.html', {"message": message})
    return render(request,'login.html')



def register(request):
    pass
    return render(request,'register.html')


def logout(request):
    pass

