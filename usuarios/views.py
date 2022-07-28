import email
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

import usuarios
from .models import Usuario
from hashlib import sha256


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})
    

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_login(request):
    
    email_login = request.POST.get('Email-login')
    senha_login = request.POST.get('Senha-login')

    senha_login = sha256 (senha_login.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email_login).filter(senha = senha_login)

    if(len(usuario) == 0):
        return redirect('/auth/login/?status=1')

    elif (len(usuario) > 0 ):
        request.session['usuario'] = usuario[0].id
        return redirect(f'/livro/home/?id_usuario={request.session["usuario"]}')

def sair(request):

    request.session.flush()
    return redirect ('/auth/login/')



def valida_cadastro(request):

    nome = request.POST.get('Nome')
    email = request.POST.get('Email')
    senha = request.POST.get('Senha')

    
    usuario = Usuario.objects.filter(email = email)


    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/login/?status=1')
        

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')


    if len(usuario) > 0:
        return redirect ('/auth/login/?status=0')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, email = email, senha = senha)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')


    except: 
        return redirect ('/auth/cadastro/?status=4')