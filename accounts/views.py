from pyexpat.errors import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        check = auth.authenticate(request, username=user, password=password)

        if check is None:
            messages.info(request,'Nome de Usuário ou senha inválidos')
            return redirect('login')
        else:
            login(request, check)
            return redirect('home')
        

    else:
        return render(request, 'paginas/login.html')


def cadastrar(request):
    try:
        check_user = User.objects.get(username = request.POST.get('username'))
        if check_user:
            messages.info(request, 'Usuário já cadastrado')
            return redirect('cad')
    except:
        if request.method == 'POST':
            user = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            passwordconfirmation = request.POST.get('password2')
            

            if user == "" or email is "" or password == "" or passwordconfirmation == "":
                messages.info(request, 'Há campos obrigatórios não preenchidos')
                return redirect('cad')

            elif password != passwordconfirmation:
                messages.info(request, 'As senhas não são iguais')
                return redirect('cad')

            elif password.isalnum() == False:
                messages.info(request, 'A senha não pode conter caracteres especiais')
                return redirect('cad')

            elif len(password) < 6 or len(password) > 12:
                messages.info(request, 'A senha deve estar entre 6 e 12 caracteres')
                return redirect('cad')

            else:
                add=User.objects.create_user(username=user, email=email, password=password)
                add.save()
                return redirect('login')

        else:
            return render(request, 'paginas/cadastrar.html')

def user_logout(request):
    logout(request)
    return redirect('login')