from django.shortcuts import render


def home_view(request):
    return render(request,'home.html')

def produtos_view(request):

    lista_produtos = [{'nome': "Monitor", "preco": 700.00, "estoque": 3},
               {'nome': "Mouse", "preco": 150.00, "estoque": 5},
               {'nome': "Teclado", "preco": 190.00, "estoque": 7},
               {'nome': "Mousepad", "preco": 200.00, "estoque": 2},
               {'nome': "Headset", "preco": 300.00, "estoque": 9},
               ]
    context = {'produtos' : lista_produtos}
    
    return render(request,'produtos.html', context)
def perfil_view(request):
    context= {'nome_usuario': 'tony' , 'cargo': 'instrutor', 'setor': 'TI'}
    return render(request, 'perfil.html', context)
def status_view(request):
    context= {'admin' : True, 'id_servidor': '127.0.0.1', 'status_sistema': '270 - online'}
    return render(request, 'status.html', context)