
import json
from django.shortcuts import render
import datetime as dt


from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly, AllowAny

from reservadebanho.models import Reserva
from base.models import Contato
from rest_api.serializers import *

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    filterset_fields = {
        'nome_pet': ['icontains'],
        'data_reserva':['gte', 'lte']
    }

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

class ContatoAgendamentoModelViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FuncionarioModelViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# @api_view([ 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({'message':f'Hello {request.data.get("name")}'})
#     return Response({'Hello':' World API'})

def inicio(request):
    reservas = Reserva.objects.all()
    dados = []
    for reserva in reservas:
        dados.append({
            'id': reserva.id,
            'nome_pet': reserva.nome_pet,
            'telefone': reserva.telefone,
            'data_reserva': reserva.data_reserva.strftime('%d/%m/%Y'), # 03/08/2023
            'observacoes': reserva.observacoes,
        })
    return HttpResponse(json.dumps(dados))

