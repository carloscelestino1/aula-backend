from django.shortcuts import render # renderizar 
from django.http import HttpResponse 

def home(request): # requisição e resposta
    return HttpResponse("teste de aula !")


def segunda(request):
    return HttpResponse('wkejhdbqkwbvdkhqgvwjkhdgvqjhwvdjqhvwdjhqvwjdhvqjwhvdjqhwvdjqhwvdjhv')


def calculo(request):
    a = 140
    b = 200
    c = a + b
    return HttpResponse(f'a resposta é:' ,c)