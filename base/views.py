from django.shortcuts import render
from django.http import HttpResponse
from base.forms import ContatoForm,  ReservaForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    sucesso = False   
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid(): 
            sucesso = True
            form.save()
    contexto = {
        'telefone': '999999',
        'responsavel': 'Maria',
        'form':form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)


# View de reserva
def reserva(request):
    sucesso = False   
    if request.method == 'GET':
        form = ReservaForm()
    else:
        form = ReservaForm(request.POST)
        if form.is_valid(): 
            sucesso = True
            form.save()
    contexto = {
        'telefone': '999999',
        'responsavel': 'Maria',
        'form':form,
        'sucesso': sucesso
    }
    return render(request, 'reserva.html', contexto)


