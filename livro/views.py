from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.

def home (request):
    if request.session.get('usuario'):
        return HttpResponse ('Primeiro comando com um fremework')
    else:
        return redirect ('/auth/login/?status=2')