from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User 
from django.contrib import auth, messages
from receitas.models import Receita

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if senha != senha2:
            print ('As senhas informadas são diferentes.')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Usuário já cadastrado.")
            print("Usuário ja cadastrado")
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print("Usuário cadastrado com sucesso.")        
        messages.success(request, "Usuário cadastrado com sucesso.")

        return redirect('login')

    else: 
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print("Os campos de email e senha não podem ficar em branco.")
            return render(request, 'usuarios/login.html') 
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso.')
                return redirect('dashboard')   
            else: 
                return render(request, 'usuarios/login.html')   

    return render(request, 'usuarios/login.html') 

def logout(request):
    auth.logout(request) 
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.filter(pessoa=id)
        dados = { 
            'receitas':receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

