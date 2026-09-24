from django.shortcuts import render
from .models import Produtos

def home_view(request):
    return render(request,'home.html')

def produtos_view(request):

    lista_produtos = Produtos.objects.all()
    context = {'produtos' : lista_produtos}
    
    return render(request,'produtos.html', context)
def perfil_view(request):
    context= {'nome_usuario': 'tony' , 'cargo': 'instrutor', 'setor': 'TI'}
    return render(request, 'perfil.html', context)
def status_view(request):
    context= {'admin' : True, 'id_servidor': '127.0.0.1', 'status_sistema': '270 - online'}
    return render(request, 'status.html', context)