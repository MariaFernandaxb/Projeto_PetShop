from django.shortcuts import render

from base.forms import ContatoForm, ReservaForm
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    formulario = ContatoForm()
    contexto = {
        'formulario': formulario
    }
    return render(request, 'contato.html', contexto)

def reserva(request):
    formulario = ReservaForm()
    contexto = {
        'formulario': formulario
    }
    return render(request, 'reserva.html', contexto)
