from django.db import models
from datetime import date

# Create your models here.

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 100)
    co_autor = models.CharField(max_length = 100, blank = True, null= True)
    data_cadastro = models.DateField(default= date.today)
    emprestado = models.BooleanField(default = False, null= True)
    nome_emprestado = models.CharField(max_length = 100, blank = True, null= True)
    data_devolucao = models.DateTimeField( blank = True, null= True)
    tempo_duracao = models.DateField(blank = True, null= True)


    class Meta:
        verbose_name = 'Livro'


    #MY DATABASE NOT FOUND