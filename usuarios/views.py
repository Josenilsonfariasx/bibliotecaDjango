import email
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('Login')


def cadastro(request):
    return render(request, 'cadastro.html')


def valida_cadastro(request):

    nome = request.POST.get('Nome')
    email = request.POST.get('Email')
    senha = request.POST.get('Senha')

    return HttpResponse ( f"{nome} {email} {senha}")

# Create your views here.
