from rest_framework.serializers import ModelSerializer

from reservadebanho.models import Reserva

from base.models import *

class AgendamentoModelSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ContatoSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'